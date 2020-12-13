from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(db.Model):
    __tablename__ = "Users"

    uId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), nullable=False)
    lastName = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    phone = db.Column(db.String(11))
    birthday = db.Column(db.Date, nullable=False)
    about = db.Column(db.Text)
    profileImg = db.Column(db.String(500))
    createDate = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False) # 0 = author - 1 = manage
    isVerifyAccount = db.Column(db.Boolean, nullable=False, default=False)