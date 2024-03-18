from flask import Flask, request, jsonify
from dataclasses import dataclass
import hashlib
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
	contacts: list = None
	groups: list = None

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'Email already in use'}), 400
	data['password'] = hashlib.sha256(data['password'].encode()).hexdigest()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = hashlib.sha256(data.get('password').encode()).hexdigest()
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	access_token = create_access_token(identity=email)
	return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required

def protected():
	return jsonify({'message': 'Access granted'}), 200

if __name__ == '__main__':
	app.run(debug=True)
