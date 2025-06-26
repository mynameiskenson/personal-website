from ..models.comment_model import Comment
from .. import db

def get_all_comments():
    """Retrieve all comments from the database."""
    return Comment.query.all()

def create_comment(content: str, post_id: int, author_id: int):
    """Create a new comment in the database."""
    new_comment = Comment(content=content, post_id=post_id, author_id=author_id)
    db.session.add(new_comment)
    db.session.commit()
    return new_comment 

def get_comment_by_id(comment_id: int):
    """Retrieve a comment by its ID."""
    return Comment.query.get(comment_id)

def update_comment(comment_id: int, content: str = None):
    """Update an existing comment."""
    comment = Comment.query.get(comment_id)
    if not comment:
        return None
    
    if content is not None:
        comment.content = content
    
    db.session.commit()
    return comment

def delete_comment(comment_id: int):
    """Delete a comment by its ID."""
    comment = Comment.query.get(comment_id)
    if not comment:
        return None
    
    db.session.delete(comment)
    db.session.commit()
    return comment

