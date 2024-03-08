from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

users = {}

@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	if username in users:
		return {'error': 'username already taken'}, 400
	password_hash = generate_password_hash(password)
	users[username] = password_hash
	return {'message': 'User created'}, 200

@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)
	password_hash = users.get(username, None)
	if password_hash is None or not check_password_hash(password_hash, password):
		return {'error': 'Invalid username or password'}, 400
	access_token = create_access_token(identity=username)
	return {'access_token': access_token}, 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
	return {'message': 'Access granted'}, 200
