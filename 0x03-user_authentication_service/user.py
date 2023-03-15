#!/usr/bin/env python3
"""create user model"""

from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import String, Column, Integer


Base = declarative_base()


class User(Base):
    """user table"""

    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String(255), nullable=False)
    hashed_password: Mapped[str] = Column(String(255), nullable=False)
    session_id: Mapped[str] = Column(String(255), nullable=True)
    reset_token: Mapped[str] = Column(String(255), nullable=True)
