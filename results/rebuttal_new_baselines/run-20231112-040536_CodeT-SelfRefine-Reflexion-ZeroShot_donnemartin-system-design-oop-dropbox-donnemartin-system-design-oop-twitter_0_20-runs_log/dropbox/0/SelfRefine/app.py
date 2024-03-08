from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management, file_management, file_sharing, security

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' in data and 'password' in data:
		return user_management.register(data)
	else:
		return {'message': 'Missing email or password'}, 400

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	if 'email' in data and 'password' in data:
		return user_management.login(data)
	else:
		return {'message': 'Missing email or password'}, 400

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if 'email' in data and 'new_password' in data:
		return user_management.forgot_password(data)
	else:
		return {'message': 'Missing email or new password'}, 400

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	if request.method == 'POST':
		data = request.get_json()
		if 'email' in data:
			return user_management.update_profile(data)
		else:
			return {'message': 'Missing email'}, 400
	else:
		return user_management.get_profile()

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	if 'name' in data and 'size' in data and 'type' in data and 'versions' in data:
		return file_management.upload(data)
	else:
		return {'message': 'Missing file data'}, 400

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	if 'name' in data:
		return file_management.download(data)
	else:
		return {'message': 'Missing file name'}, 400

@app.route('/organize', methods=['POST'])
def organize():
	data = request.get_json()
	if 'name' in data:
		return file_management.organize(data)
	else:
		return {'message': 'Missing file name'}, 400

@app.route('/versioning', methods=['GET', 'POST'])
def versioning():
	if request.method == 'POST':
		data = request.get_json()
		if 'name' in data and 'version' in data:
			return file_management.update_version(data)
		else:
			return {'message': 'Missing file name or version'}, 400
	else:
		return file_management.get_version()

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	if 'file_name' in data and 'shared_with' in data and 'permissions' in data:
		return file_sharing.share(data)
	else:
		return {'message': 'Missing share data'}, 400

@app.route('/activity_log', methods=['GET'])
def activity_log():
	return security.get_activity_log()

if __name__ == '__main__':
	app.run(debug=True)
