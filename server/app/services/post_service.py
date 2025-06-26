from ..models.post_model import Post
from .. import db

def get_all_posts():
    """Retrieve all posts from the database."""
    return Post.query.all()

def create_post(title: str, subtitle: str, content: str, author_id: int):
    """Create a new post in the database."""
    new_post = Post(title=title, subtitle=subtitle, content=content, author_id=author_id)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_post_by_id(post_id: int):
    """Retrieve a post by its ID."""
    return Post.query.get(post_id)

def update_post(post_id: int, title: str = None, subtitle: str = None, content: str = None):
    """Update an existing post."""
    post = Post.query.get(post_id)
    if not post:
        return None
    
    if title is not None:
        post.title = title
    if subtitle is not None:
        post.subtitle = subtitle
    if content is not None:
        post.content = content
    
    db.session.commit()
    return post

def delete_post(post_id: int):
    """Delete a post by its ID."""
    post = Post.query.get(post_id)
    if not post:
        return None
    
    db.session.delete(post)
    db.session.commit()
    return post 