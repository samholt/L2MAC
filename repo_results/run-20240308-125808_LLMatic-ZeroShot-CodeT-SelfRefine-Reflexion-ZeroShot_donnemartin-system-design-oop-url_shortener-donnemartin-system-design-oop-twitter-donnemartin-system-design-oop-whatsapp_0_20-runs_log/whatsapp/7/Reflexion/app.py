from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
sessions = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	sessions[email] = 'Logged in'
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/logout', methods=['POST'])
def logout():
	data = request.get_json()
	email = data.get('email')
	sessions.pop(email, None)
	return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	# In a real application, send email to user with password reset link
	return jsonify({'message': 'Password reset link sent to email'}), 200

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	email = data.get('email')
	profile_picture = data.get('profile_picture')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.profile_picture = profile_picture
	return jsonify({'message': 'Profile picture set successfully'}), 200

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	email = data.get('email')
	status_message = data.get('status_message')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.status_message = status_message
	return jsonify({'message': 'Status message set successfully'}), 200

@app.route('/set_privacy_settings', methods=['POST'])
def set_privacy_settings():
	data = request.get_json()
	email = data.get('email')
	privacy_settings = data.get('privacy_settings')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.privacy_settings = privacy_settings
	return jsonify({'message': 'Privacy settings set successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
