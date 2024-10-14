from flask import Flask
from database.database import db
from database.config import Config
from flask_socketio import SocketIO
from views import message_view
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

Migrate(app, db)
db.init_app(app)
socketio = SocketIO(app)

# Blueprintを登録
app.register_blueprint(message_view.message_view)

# WebSocketのイベントを受信
socketio.on_namespace(message_view.MessageController("/message"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # 開発用サーバとしてeventletを使用
    socketio.run(app, host="0.0.0.0", port=5500, debug=True)
