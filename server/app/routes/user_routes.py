from flask import Blueprint, request, jsonify
from ..services.user_service import (
    get_all_users, 
    create_user, 
    get_user_by_id, 
    update_user
)
from ..schemas.user_schema import UserSchema

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/', methods=['GET'])
def index():
    """Retrieve all users."""
    users = get_all_users()
    return users_schema.jsonify(users)

@user_bp.route('/', methods=['POST'])
def create():
    """Create a new user."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        user = create_user(
            username=data['username'],
            email=data['email'],
            password_hash=data['password']
        )
        return user_schema.jsonify(user), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route('/<int:user_id>', methods=['GET'])
def show(user_id):
    """Retrieve a user by their ID."""
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return user_schema.jsonify(user)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update(user_id):
    """Update an existing user."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    user = update_user(
        user_id,
        username=data.get('username'),
        email=data.get('email'),
        password_hash=data.get('password')
    )
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return user_schema.jsonify(user)
