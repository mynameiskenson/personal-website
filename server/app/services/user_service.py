from ..models.user_model import User
from .. import db
from werkzeug.security import generate_password_hash


def get_all_users():
    """Retrieve all users from the database."""
    return User.query.all()

def create_user(username: str, email: str, password_hash: str):
    """Create a new user in the database."""
    g_password_hash = generate_password_hash(password_hash, method="pbkdf2:sha256", salt_length=8)
    new_user = User(username=username, email=email, password_hash=g_password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_id(user_id: int):
    """Retrieve a user by their ID."""
    return User.query.get(user_id)

def update_user(user_id: int, username: str = None, email: str = None, password_hash: str = None):
    """Update an existing user."""
    user = User.query.get(user_id)
    if not user:
        return None
    
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    if password_hash is not None:
        user.password_hash = generate_password_hash(password_hash, method="pbkdf2:sha256", salt_length=8)
    
    db.session.commit()
    return user

def delete_user(user_id: int):
    """Delete a user by their ID."""
    user = User.query.get(user_id)
    if not user:
        return None
    
    db.session.delete(user)
    db.session.commit()
    return user # user deleted successfully or None if not found
