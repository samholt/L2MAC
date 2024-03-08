from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management
import file_management
import file_sharing

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return jsonify(user_management.register(data))

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return jsonify(user_management.login(data))

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	return jsonify(user_management.forgot_password(data))

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	return jsonify(user_management.profile(data))

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	return jsonify(file_management.upload(data))

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	return jsonify(file_management.download(data))

@app.route('/organize', methods=['POST'])
def organize():
	data = request.get_json()
	return jsonify(file_management.organize(data))

@app.route('/versioning', methods=['GET'])
def versioning():
	data = request.get_json()
	return jsonify(file_management.versioning(data))

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	return jsonify(file_sharing.share(data))

@app.route('/shared_folders', methods=['GET'])
def shared_folders():
	data = request.get_json()
	return jsonify(file_sharing.shared_folders(data))

if __name__ == '__main__':
	app.run(debug=True)
