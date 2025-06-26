from app.extensions import ma
from ..models.user_model import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True  # Include foreign keys in the serialized output
        ordered = True  # Maintain the order of fields in the output
        dump_only = ("password_hash",)  # Exclude password hash from serialization