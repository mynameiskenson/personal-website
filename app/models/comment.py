from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime as dt

from app import db

class Comment(db.Model):
    __tablename__ = "comments"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at : Mapped[dt.datetime] = mapped_column(DateTime, nullable=False)
    author_id : Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["User"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"), nullable=False)
    post: Mapped["BlogPost"] = relationship(back_populates="comments")