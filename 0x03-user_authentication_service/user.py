#!/usr/bin/env python3
"""create user model"""

from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String


Base = declarative_base()


class User(Base):
    """user table"""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)
    session_id: Mapped[str] = mapped_column(String(250), nullable=True)
    reset_token: Mapped[str] = mapped_column(String(250), nullable=True)
