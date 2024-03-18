from flask import Flask, request
from models.user import User
import secrets

app = Flask(__name__)

# Mock database
users_db = {}

# Mock token storage
reset_tokens = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if not username or not email or not password:
		return {'message': 'Missing data'}, 400
	if username in users_db or any(u.email == email for u in users_db.values()):
		return {'message': 'User already exists'}, 400
	new_user = User(username, email, password)
	users_db[username] = new_user
	return {'message': 'User created successfully'}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if not username or not password:
		return {'message': 'Missing data'}, 400
	user = users_db.get(username)
	if not user or not user.check_password(password):
		return {'message': 'Invalid credentials'}, 401
	# For simplicity, we return username as token
	return {'token': username}, 200

@app.route('/password_reset_request', methods=['POST'])
def password_reset_request():
	data = request.get_json()
	email = data.get('email')
	if not email:
		return {'message': 'Missing data'}, 400
	user = next((u for u in users_db.values() if u.email == email), None)
	if not user:
		return {'message': 'User not found'}, 404
	# Generate a password reset token
	token = secrets.token_urlsafe()
	# Store the token
	reset_tokens[token] = user.username
	# Mock sending an email
	print(f'Send email to {email} with reset token {token}')
	return {'message': 'Password reset email sent'}, 200

@app.route('/password_reset', methods=['POST'])
def password_reset():
	data = request.get_json()
	token = data.get('token')
	new_password = data.get('new_password')
	if not token or not new_password:
		return {'message': 'Missing data'}, 400
	username = reset_tokens.get(token)
	if not username:
		return {'message': 'Invalid token'}, 400
	user = users_db.get(username)
	if not user:
		return {'message': 'User not found'}, 404
	# Update the user's password
	user.set_password(new_password)
	# Remove the token
	del reset_tokens[token]
	return {'message': 'Password reset successfully'}, 200
