from database.database import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
        }
