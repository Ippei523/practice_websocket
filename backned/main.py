from flask import Flask, render_template
from backned.models.message_model import db
from flask_socketio import SocketIO, emit
from backned.views import message_view

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
db.init_app(app)
socketio = SocketIO(app)

# Blueprintを登録
app.register_blueprint(message_view.message_view)

# WebSocketのイベントを受信
socketio.on_namespace(message_view.MessageController("/message"))


if __name__ == "__main__":
    # 開発用サーバとしてeventletを使用
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
