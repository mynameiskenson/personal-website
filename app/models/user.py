from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import datetime as dt

from app import db

class User(db.Model):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    posts: Mapped[List["BlogPost"]] = relationship(back_populates="author")