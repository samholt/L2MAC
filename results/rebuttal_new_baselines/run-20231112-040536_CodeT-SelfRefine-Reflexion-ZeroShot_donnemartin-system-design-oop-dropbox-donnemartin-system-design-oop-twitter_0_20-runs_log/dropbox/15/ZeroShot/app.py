from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management
import file_management
import file_sharing
import security

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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	data = request.get_json()
	if request.method == 'POST':
		return jsonify(user_management.update_profile(data))
	else:
		return jsonify(user_management.get_profile(data))

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

@app.route('/versioning', methods=['GET', 'POST'])
def versioning():
	data = request.get_json()
	if request.method == 'POST':
		return jsonify(file_management.restore_version(data))
	else:
		return jsonify(file_management.get_versions(data))

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	return jsonify(file_sharing.share(data))

@app.route('/activity', methods=['GET'])
def activity():
	data = request.get_json()
	return jsonify(security.get_activity(data))

if __name__ == '__main__':
	app.run(debug=True)
