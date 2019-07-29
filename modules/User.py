import sqlite3
from flask_sqlalchemy import model
from db import db
class UserModel(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))


    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    def __init__(self,username,password):
        self.username = username
        self.password = password


    @classmethod
    def findBy_username(cls,username):
         user=cls.query.filter_by(username=username).first()
         return user

    @classmethod
    def findBy_id(cls,_id):
        user= cls.query.filter_by(id=_id).first()
        return user

    def add_user(self):
        db.session.add(self)
        db.session.commit()