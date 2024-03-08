from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from dataclasses import dataclass

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mocking a database with an in memory dictionary
database = {}

@dataclass
class User:
	email: str
	username: str
	password: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(email=data['email'], username=data['username'], password=data['password'])
	database[data['username']] = new_user
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = database.get(data['username'])
	if user and user.password == data['password']:
		access_token = create_access_token(identity=data['username'])
		return jsonify(access_token=access_token), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
	current_user = get_jwt_identity()
	user = database.get(current_user)
	if user:
		return jsonify(user), 200
	return jsonify({'message': 'User not found'}), 404
