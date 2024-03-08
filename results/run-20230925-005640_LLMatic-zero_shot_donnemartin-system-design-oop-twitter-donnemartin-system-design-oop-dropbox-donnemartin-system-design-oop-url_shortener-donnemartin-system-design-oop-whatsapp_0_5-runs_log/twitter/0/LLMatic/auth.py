from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash
from database import users_db, user_schema

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'  # Change this!

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	for field in user_schema:
		if field not in data:
			return {'message': f'Missing field: {field}'}, 400

	if data['email'] in users_db:
		return {'message': 'Email already registered.'}, 400

	data['password'] = generate_password_hash(data['password'])
	users_db[data['email']] = data

	return {'message': 'User created.'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data.get('email'))

	if not user or not check_password_hash(user['password'], data.get('password')):
		return {'message': 'Invalid credentials.'}, 401

	return {'access_token': user['email']}, 200
