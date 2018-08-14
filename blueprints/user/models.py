from extensions import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,index=True,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    phone=db.Column(db.String,unique=True,nullable=True)
    password=db.Column(db.String,unique=True)
    image=db.Column(db.String,unique=True,nullable=True)
    role=db.Column(db.Integer,default=0)#0 is viewwer 1 is commedian 2is admin 3 is bkdoor