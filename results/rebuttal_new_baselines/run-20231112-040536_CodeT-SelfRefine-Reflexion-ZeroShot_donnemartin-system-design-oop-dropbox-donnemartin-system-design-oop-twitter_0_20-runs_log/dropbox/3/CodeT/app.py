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

@app.route('/create_folder', methods=['POST'])
def create_folder():
	data = request.get_json()
	return file_management.create_folder(data)

@app.route('/rename_file', methods=['POST'])
def rename_file():
	data = request.get_json()
	return file_management.rename_file(data)

@app.route('/move_file', methods=['POST'])
def move_file():
	data = request.get_json()
	return file_management.move_file(data)

@app.route('/delete_file', methods=['DELETE'])
def delete_file():
	data = request.get_json()
	return file_management.delete_file(data)

@app.route('/generate_link', methods=['POST'])
def generate_link():
	data = request.get_json()
	return file_sharing.generate_link(data)

@app.route('/invite_user', methods=['POST'])
def invite_user():
	data = request.get_json()
	return file_sharing.invite_user(data)

@app.route('/set_permission', methods=['POST'])
def set_permission():
	data = request.get_json()
	return file_sharing.set_permission(data)

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
