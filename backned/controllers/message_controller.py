from flask_socketio import Namespace, emit
from backned.models.message_model import Message, db


class MessageController(Namespace):
    def on_get_messages(self):
        print("get_messages")
        message = Message.query.all()
        messages = [m.to_dict() for m in message]
        emit("get_messages", messages)

    def on_post_message(self, data):
        print("post_message")
        message = Message(data["message"], data["date"], data["user_id"])
        db.session.add(message)
        db.session.commit()
        emit("post_message", message.to_dict(), broadcast=True)

    @staticmethod
    def get_all_messages():
        message = Message.query.all()
        messages = [m.to_dict() for m in message]
        return messages

    @staticmethod
    def create_message(data):
        message = Message(data["message"], data["date"], data["user_id"])
        db.session.add(message)
        db.session.commit()
        return message.to_dict()
