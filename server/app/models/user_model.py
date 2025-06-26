from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime as dt

from app.extensions import db

if TYPE_CHECKING:
    from app.models.post_model import Post
    from app.models.comment_model import Comment

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), onupdate=dt.datetime.now(dt.timezone.utc), nullable=False)

    # Relationships
    posts: Mapped[list[Post]] = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments: Mapped[list[Comment]] = relationship("Comment", back_populates="author", cascade="all, delete-orphan")