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
	user = user_management.register(data)
	return jsonify(user), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = user_management.login(data)
	return jsonify(user), 200

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	user = user_management.get_profile(data)
	return jsonify(user), 200

@app.route('/upload', methods=['POST'])
def upload():
	data = request.get_json()
	file = file_management.upload(data)
	return jsonify(file), 201

@app.route('/download', methods=['GET'])
def download():
	data = request.get_json()
	file = file_management.download(data)
	return jsonify(file), 200

@app.route('/share', methods=['POST'])
def share():
	data = request.get_json()
	link = file_sharing.share(data)
	return jsonify(link), 201

@app.route('/activity', methods=['GET'])
def activity():
	data = request.get_json()
	log = security.get_activity_log(data)
	return jsonify(log), 200

if __name__ == '__main__':
	app.run(debug=True)
