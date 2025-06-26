from __future__ import annotations
from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime as dt

from app.extensions import db

if TYPE_CHECKING:
    from app.models.post_model import Post
    from app.models.user_model import User

class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime, default=dt.datetime.now(dt.timezone.utc), onupdate=dt.datetime.now(dt.timezone.utc), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    # Relationships
    post: Mapped[Post] = relationship("Post",back_populates="comments")
    author: Mapped[User] = relationship("User", back_populates="comments")