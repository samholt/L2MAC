from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management, file_management, file_sharing, security

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if not data or 'email' not in data or 'password' not in data:
		return {'message': 'Missing email or password'}, 400
	return user_management.register(data)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if not data or 'email' not in data or 'password' not in data:
		return {'message': 'Missing email or password'}, 400
	return user_management.login(data)

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if not data or 'email' not in data or 'new_password' not in data:
		return {'message': 'Missing email or new password'}, 400
	return user_management.forgot_password(data)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	if request.method == 'POST':
		data = request.get_json()
		if not data or 'email' not in data:
			return {'message': 'Missing email'}, 400
		return user_management.update_profile(data)
	else:
		return user_management.get_profile()

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	if not data or 'name' not in data or 'content' not in data:
		return {'message': 'Missing file name or content'}, 400
	return file_management.upload(data)

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	if not data or 'name' not in data:
		return {'message': 'Missing file name'}, 400
	return file_management.download(data)

@app.route('/organize', methods=['POST'])
def organize():
	data = request.get_json()
	if not data or 'name' not in data or 'new_name' not in data:
		return {'message': 'Missing file name or new name'}, 400
	return file_management.organize(data)

@app.route('/versioning', methods=['GET', 'POST'])
def versioning():
	if request.method == 'POST':
		data = request.get_json()
		if not data or 'name' not in data or 'new_version' not in data:
			return {'message': 'Missing file name or new version'}, 400
		return file_management.update_version(data)
	else:
		return file_management.get_version()

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	if not data or 'file_name' not in data or 'shared_with' not in data or 'permissions' not in data:
		return {'message': 'Missing file name, shared with, or permissions'}, 400
	return file_sharing.share(data)

@app.route('/activity_log', methods=['GET'])
def activity_log():
	return security.get_activity_log()

if __name__ == '__main__':
	app.run(debug=True)
