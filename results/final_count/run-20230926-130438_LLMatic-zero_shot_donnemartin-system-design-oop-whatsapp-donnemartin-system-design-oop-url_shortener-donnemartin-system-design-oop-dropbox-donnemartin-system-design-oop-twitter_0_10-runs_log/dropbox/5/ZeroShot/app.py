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
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data['email']
	password = data['password']
	if email in users and users[email].password == password:
		return jsonify({'message': 'Login successful'}), 200
	else:
		return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = FileManager(data['name'], data['type'], data['size'], data['content'])
	files[file.name] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download', methods=['GET'])
def download():
	file_name = request.args.get('name')
	if file_name in files:
		return jsonify({'message': 'File downloaded successfully', 'file': files[file_name].to_dict()}), 200
	else:
		return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
