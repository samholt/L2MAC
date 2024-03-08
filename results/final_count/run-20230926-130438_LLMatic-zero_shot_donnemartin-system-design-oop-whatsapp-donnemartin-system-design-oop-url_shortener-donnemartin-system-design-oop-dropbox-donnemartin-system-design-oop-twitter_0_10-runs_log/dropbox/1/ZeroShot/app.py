from flask import Flask, request, jsonify
from user import User
from file_manager import FileManager

app = Flask(__name__)

users = {}
files = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['name'], data['email'], data['password'])
	users[data['email']] = user
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email in users and users[email].password == password:
		return jsonify(users[email].to_dict()), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	email = data['email']
	if email in users:
		return jsonify(users[email].to_dict()), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file_manager = FileManager(data['file'], data['user_email'])
	files[data['file']['name']] = file_manager
	return jsonify(file_manager.to_dict()), 201

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file_name = data['file_name']
	if file_name in files:
		return jsonify(files[file_name].to_dict()), 200
	else:
		return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
