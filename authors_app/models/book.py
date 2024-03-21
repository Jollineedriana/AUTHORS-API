from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authors_app.extensions import db
from datetime import datetime

from flask_migrate import Migrate


# from authors_app import db
from authors_app.extensions import db


class Books(db.Model):
 __tablename__="books"
 id =db.Column(db.Integer,primary_key=True)
 title=db.Column(db.String(50),nullable=False)
 description=db.Column(db.String(100),nullable=False)
 image=db.Column(db.String(255),nullable=False)
 price=db.Column(db.Integer,nullable=False)
 number_of_pages=db.Column(db.Integer,nullable=False) 
 user_id =db.Column(db.Integer, db.ForeignKey("Users.id"))
 #user=db.relationship('User',backref='books')
    
    
def __init__(self, title, description, pages, users_id, price, user_id, image=None):
        self.users_id = users_id
        self.pages = pages
        self.title = title
        self.description = description
        self.users_id = users_id
        self.price = price
        self.image = image