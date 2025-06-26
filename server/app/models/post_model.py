from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime as dt

from app.extensions import db

if TYPE_CHECKING:
    from app.models.user_model import User
    from app.models.comment_model import Comment

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), onupdate=dt.datetime.now(dt.timezone.utc), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    # Relationships
    author: Mapped[User] = relationship("User", back_populates="posts")
    comments: Mapped[list[Comment]] = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
        