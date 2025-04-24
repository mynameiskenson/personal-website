from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
import datetime as dt

from app import db

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime, nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)