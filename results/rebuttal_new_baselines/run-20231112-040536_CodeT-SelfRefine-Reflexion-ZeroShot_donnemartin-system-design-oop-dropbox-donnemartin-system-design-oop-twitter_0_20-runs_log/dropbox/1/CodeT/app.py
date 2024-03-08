from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management, file_management, file_sharing, security

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return user_management.register(data)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return user_management.login(data)

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	return user_management.forgot_password(data)

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	return user_management.profile(data)

@app.route('/change_password', methods=['POST'])
def change_password():
	data = request.get_json()
	return user_management.change_password(data)

@app.route('/upload_file', methods=['POST'])
def upload_file():
	data = request.get_json()
	return file_management.upload_file(data)

@app.route('/download_file', methods=['GET'])
def download_file():
	data = request.get_json()
	return file_management.download_file(data)

@app.route('/organize_file', methods=['POST'])
def organize_file():
	data = request.get_json()
	return file_management.organize_file(data)

@app.route('/version_file', methods=['GET'])
def version_file():
	data = request.get_json()
	return file_management.version_file(data)

@app.route('/share_link', methods=['POST'])
def share_link():
	data = request.get_json()
	return file_sharing.share_link(data)

@app.route('/shared_folder', methods=['POST'])
def shared_folder():
	data = request.get_json()
	return file_sharing.shared_folder(data)

@app.route('/encrypt_file', methods=['POST'])
def encrypt_file():
	data = request.get_json()
	return security.encrypt_file(data)

@app.route('/activity_log', methods=['GET'])
def activity_log():
	data = request.get_json()
	return security.activity_log(data)

if __name__ == '__main__':
	app.run(debug=True)
