from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from authors_app.extensions import db


class Company (db.Model):
    __tablename__ = "companies"
    id =  db.Column(db.Integer, primary_key= True)
    title = db.Column (db.String(100), nullable=False)
    pages = db.Column (db.Integer)
    description = db.Column (db.String(100))
    user_id = db.Column (db.Integer, db.ForeignKey("Users.id"))
    company = db.Column (db.Integer, db.ForeignKey("companies.id"))
    created_at = db.Column (db.DateTime, default=datetime.now())
    updated_at = db.Column (db.DateTime, onupdate=datetime.now())
