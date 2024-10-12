from flask import Blueprint, jsonify, request
from controllers.message_controller import MessageController

message_view = Blueprint("message_view", __name__, url_prefix="/api")


@message_view.route("/messages", methods=["GET"])
def get_messages():
    messages = MessageController.get_all_messages()
    return jsonify([message.to_dict() for message in messages])


@message_view.route("/messages", methods=["POST"])
def post_message():
    try:
        data = request.json
        content = data.get("content", "")
        if not content:
            return jsonify({"error": "Content must not be empty"}), 400

        new_message = MessageController.create_message(content)
        return jsonify(new_message.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
