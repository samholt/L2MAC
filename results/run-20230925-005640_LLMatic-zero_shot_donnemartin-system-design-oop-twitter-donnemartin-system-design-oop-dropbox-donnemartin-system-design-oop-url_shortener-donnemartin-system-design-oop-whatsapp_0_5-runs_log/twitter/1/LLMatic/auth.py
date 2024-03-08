from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(email=data['email'], username=data['username'], password=generate_password_hash(data['password']))
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and check_password_hash(user.password, data['password']):
		access_token = create_access_token(identity={'email': user.email})
		return jsonify({'access_token': access_token}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401
