from app.extensions import ma
from ..models.comment_model import Comment

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True
        include_fk = True  # Include foreign keys in the serialized output
        ordered = True  # Maintain the order of fields in the output
        dump_only = ("created_at", "updated_at")  # Exclude timestamps from serialization