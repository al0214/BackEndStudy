import pathlib
from typing import Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
import uvicorn
from sqlalchemy.orm import Session

DATABASE_URL = "mysql+pymysql://root:1234@localhost/db_name"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True, index=True)

    email = Column(String(150))

class UserCreate(BaseModel):
    username: str
    email: str

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(username=user.username, email=user.email)
    db.add(new_user)

    db.commit()
    db.refresh(new_user)

    return {"id": new_user.id, "username": new_user.username, "email": new_user.email}

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}

    if user.username is not None:
        db_user.username = user.username
    if user.email is not None:
        db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User). filter(User.id == user_id).first()
    if db_user is None:
        return {"error": "User not found"}

    db.delete(db_user)
    db.commit()
    return {"message":"success delete user"}


if __name__  == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8080, reload=True)