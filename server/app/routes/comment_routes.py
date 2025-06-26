from flask import Blueprint, request, jsonify
from ..services.comment_service import (
    get_all_comments,
    create_comment,
    get_comment_by_id,
    update_comment,
    delete_comment
)
from ..schemas.comment_schema import CommentSchema

comment_bp = Blueprint('comment_bp', __name__)
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@comment_bp.route('/', methods=['GET'])
def index():
    """Retrieve all comments."""
    comments = get_all_comments()
    return comments_schema.jsonify(comments)

@comment_bp.route('/', methods=['POST'])
def create():
    """Create a new comment."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        comment = create_comment(
            content=data['content'],
            post_id=data['post_id'],
            author_id=data['author_id']
        )
        return comment_schema.jsonify(comment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@comment_bp.route('/<int:comment_id>', methods=['GET'])
def show(comment_id):
    """Retrieve a comment by its ID."""
    comment = get_comment_by_id(comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404
    return comment_schema.jsonify(comment)

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update(comment_id):
    """Update an existing comment."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    comment = update_comment(
        comment_id,
        content=data.get('content')
    )
    
    if not comment:
        return jsonify({"error": "Comment not found"}), 404
    
    return comment_schema.jsonify(comment)

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete(comment_id):
    """Delete a comment by its ID."""
    comment = delete_comment(comment_id)
    if not comment:
        return jsonify({"error": "Comment not found"}), 404
    return jsonify({"message": "Comment deleted successfully"}), 204

