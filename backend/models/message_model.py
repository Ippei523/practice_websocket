from database.database import db


class Message(db.Model):
    __tablename__ = "message"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, message, date, user_id):
        super().__init__()
        self.message = message
        self.date = date
        self.user_id = user_id

    def __repr__(self):
        return f"<Message {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "date": self.date.strftime("%Y/%m/%d %H:%M:%S"),
            "user_id": self.user_id,
        }
