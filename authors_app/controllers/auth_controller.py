from flask import Blueprint, request, jsonify, json
from datetime import datetime
from authors_app.extensions import db,Bcrypt
from authors_app.models.users import User

from flask import Blueprint, request, jsonify
from authors_app.extensions import db, bcrypt
from authors_app.models.users import User

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
def register():
    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        contact = request.json['contact']
        password = request.json['password']
        
        # Basic validation
        if not first_name:
            return jsonify({"error": "Your first name is required"}), 400
        if not last_name:
            return jsonify({"error": "Your last name is required"}), 400
        if not email:
            return jsonify({"error": "Your email is required"}), 400
        if not contact:
            return jsonify({"error": "Your contact is required"}), 400
        if len(password) < 6:
            return jsonify({"error": "Your password must have more than six characters"}), 400
        
        # Check if the user already exists
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "This email is already registered"}), 409
        if User.query.filter_by(contact=contact).first():
            return jsonify({"error": "This contact is already registered"}), 409
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create a new user instance
        new_user = User(
            first_name=first_name, 
            last_name=last_name, 
            email=email,
            contact=contact, 
            password=hashed_password  # Store the hashed password
        )

        # Add and commit the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Build a success response
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

auth = Blueprint('auth', __name__, url_prefix='/api/vl/auth')

@auth.route('/register',  methods=['POST'])
#create a function for the user
def register():
 try: 
    first_name= request.json['first_name'] 
    last_name=request.json['last_name']
    email=request.json['email']
    contact=request.json['contact']
    password=request.json['password']
    # user_type=request.json['user_type']
    # biography=request.json['biography']
    # image=request.json['image']
    
    hashed_password = bcrypt.generate_password_hash(password)
    
    if not first_name:
        return jsonify({"error":"Your first name is required"})
    # if not image:
    #     return jsonify({"error":"Your image is required"})
    if not last_name:
        return jsonify({"error":"Your last name is required"})
    if not email:
        return jsonify({"error":"Your email is required"})
    if not contact:
        return jsonify({"error":"Your contact is required"})
    # if not user_type:
    #     return jsonify({"error":"User type is required"})
    if  len(password)<6:
        return jsonify({"error":"Your password must have more than six characters"})
    if not email:
        return jsonify({"error":"Your email is required"})
    # my_dict = {
    #     first_name, last_name,email,contact,user_type,image
    # }
    # serialized_dict = list(my_dict)
    # return jsonify(serialized_dict)
    # if user_type=='author' and not biography:
    #     return jsonify({"Your biography is required"})
    #checking if an object has already been registered
    if User.query.filter_by(email=email).first():
        return jsonify({"error","This email is already registered"})
    if User.query.filter_by(contact=contact).first():
        return jsonify({"error","This contact is already registered"})
    
    
   # Creating a new user
    
    new_user = User(first_name=first_name, last_name=last_name, email=email,
                        contact=contact, password=hashed_password
                       )

        # Adding and committing to the database
    db.session.add(new_user)
    db.session.commit()

        # Building a response
    username = new_user.get_full_name()

    return jsonify({'message':'User created successfully'}),201
        #     'message': f'{username} has been successfully created as a {new_user.user_type}',
        #      'user': {
        #         'first_name': new_user.first_name,
        #         'last_name': new_user.last_name,
        #         'email': new_user.email,
        #         'contact': new_user.contact,
        #         'type': new_user.user_type,
        #         'image':new_user.image
                
                
        #     }
        # })

 except Exception as e:
    db.session.rollback()
    return jsonify({'error': str(e)})
    
        
    
    