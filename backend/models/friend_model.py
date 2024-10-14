from database.database import db


class Friend(db.Model):
    __tablename__ = "friend"

    id = db.Column(db.Integer, primary_key=True)
    # user_id is the id of the user who sent the friend request
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # friend_id is the id of the user who received the friend request
    friend_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, user_id, friend_id):
        super().__init__()
        self.user_id = user_id
        self.friend_id = friend_id

    def __repr__(self):
        return f"<Friend {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "friend_id": self.friend_id,
        }

    def to_dict_with_user(self, user):
        return {
            "id": self.id,
            "user": user.to_dict(),
        }
