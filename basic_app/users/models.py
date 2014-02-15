from basic_app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    age = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name
