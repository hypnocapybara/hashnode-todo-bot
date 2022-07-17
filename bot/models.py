from gino import Gino
from sqlalchemy import func

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    telegram_user_id = db.Column(db.String(length=200))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.Column(db.String(length=255))
    last_name = db.Column(db.String(length=255))
    username = db.Column(db.String(length=255))


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    text = db.Column(db.Text)
