from flask import Flask, request, jsonify
from services.user_service import register_user, login_user, forgot_password, get_user_profile, change_password

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = register_user(data['name'], data['email'], data['password'], data['profile_picture'])
	return jsonify(user.__dict__), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = login_user(data['email'], data['password'])
	if user:
		return jsonify(user.__dict__), 200
	return 'Invalid credentials', 401

@app.route('/forgot_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	if forgot_password(data['email'], data['new_password']):
		return 'Password reset successful', 200
	return 'User not found', 404

@app.route('/profile/<email>', methods=['GET'])
def profile(email):
	user = get_user_profile(email)
	if user:
		return jsonify(user.__dict__), 200
	return 'User not found', 404

@app.route('/change_password', methods=['POST'])
def update_password():
	data = request.get_json()
	if change_password(data['email'], data['old_password'], data['new_password']):
		return 'Password change successful', 200
	return 'Invalid credentials', 401

if __name__ == '__main__':
	app.run(debug=True)
