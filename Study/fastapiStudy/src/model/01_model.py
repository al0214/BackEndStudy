from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, comment='기본 키')

    username = Column(String(50), unique=True, nullable=False, comment="이메일 주소")

    email = Column(String(120), unique=True, nullable=False, comment="이메일 주소")

    is_active = Column(Boolean, default=True, comment="활성 상태")

    created_at = Column(DateTime, default=datetime.utcnow, comment="생성 타임스탬프")

    grade = Column(Float, comment="사용자 등급")

    parent_id = Column(Integer, ForeignKey('parents.id'), comment="상위 ID")




