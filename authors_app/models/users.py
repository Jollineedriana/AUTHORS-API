from authors_app.extensions import db
from datetime import datetime
from authors_app.extensions import  Migrate


class User(db.Model): # The model must be a captial letter
    __tablename__ = 'Users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.String(50), unique=True)
    # image = db.Column(db.String(255), nullable=True)
    # user_type = db.Column(db.String(100), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.now())
    update_at = db.Column(db.DateTime, onupdate=datetime.now())
    password = db.Column(db.String(100), nullable=False, unique=True)
    
    
    def __init__(self,first_name,last_name,password,email,contact):
        self.first_name=first_name
        self.last_name=last_name
        self.email= email
        self.contact= contact
        # self.image= image
        # self.biography=biography
        self.password=password
        # self.user_type=user_type

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'