from flask import Blueprint, request, jsonify
from ..services.post_service import (
    get_all_posts, 
    create_post, 
    get_post_by_id, 
    update_post, 
    delete_post
)
from ..schemas.post_schema import PostSchema

post_bp = Blueprint('post_bp', __name__)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@post_bp.route('/', methods=['GET'])
def index():
    """Retrieve all posts."""
    posts = get_all_posts()
    return posts_schema.jsonify(posts)

@post_bp.route('/', methods=['POST'])
def create():
    """Create a new post."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        post = create_post(
            title=data['title'],
            content=data['content'],
            author_id=data['author_id']
        )
        return post_schema.jsonify(post), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@post_bp.route('/<int:post_id>', methods=['GET'])
def show(post_id):
    """Retrieve a post by its ID."""
    post = get_post_by_id(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return post_schema.jsonify(post)

@post_bp.route('/<int:post_id>', methods=['PUT'])
def update(post_id):
    """Update an existing post."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    post = update_post(
        post_id,
        title=data.get('title'),
        content=data.get('content')
    )
    
    if not post:
        return jsonify({"error": "Post not found"}), 404
    
    return post_schema.jsonify(post)

@post_bp.route('/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    """Delete a post by its ID."""
    post = delete_post(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    
    return jsonify({"message": "Post deleted successfully"}), 200