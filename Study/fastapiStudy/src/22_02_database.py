import pathlib

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
import uvicorn
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:1234@localhost/db_name"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True, index=True)

    email = Column(String(150))

class UserCreate(BaseModel):
    username: str
    email: str


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/users/")
def create_user(user: UserCreate):

    db = SessionLocal()

    db_user = User(username=user.username, email=user.email)

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    db.close()

    return {"id": db_user.id, "username": db_user.username, "email": db_user.email}

if __name__  == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8080, reload=True)