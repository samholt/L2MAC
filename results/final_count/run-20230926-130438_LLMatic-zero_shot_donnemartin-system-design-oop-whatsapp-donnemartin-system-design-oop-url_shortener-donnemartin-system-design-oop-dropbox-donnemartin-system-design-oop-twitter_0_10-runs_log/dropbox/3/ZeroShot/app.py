from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
files = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if data['email'] in users:
		return jsonify({'message': 'User already exists'}), 400
	users[data['email']] = {'name': data['name'], 'password': data['password'], 'files': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if data['email'] not in users or users[data['email']]['password'] != data['password']:
		return jsonify({'message': 'Invalid email or password'}), 400
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	if data['email'] not in users:
		return jsonify({'message': 'User does not exist'}), 400
	files[data['filename']] = {'content': data['content'], 'owner': data['email']}
	users[data['email']]['files'].append(data['filename'])
	return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/download', methods=['GET'])
def download():
	filename = request.args.get('filename')
	if filename not in files:
		return jsonify({'message': 'File does not exist'}), 400
	return jsonify({'content': files[filename]['content']}), 200

if __name__ == '__main__':
	app.run(debug=True)
