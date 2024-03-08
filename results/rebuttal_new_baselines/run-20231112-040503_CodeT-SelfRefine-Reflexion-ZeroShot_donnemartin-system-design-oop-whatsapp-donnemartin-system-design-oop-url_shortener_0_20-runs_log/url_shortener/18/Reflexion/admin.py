from flask import Flask, request, jsonify
from models import User, UrlData
from auth import users
from url_shortener import url_data

app = Flask(__name__)

@app.route('/admin', methods=['GET'])
def admin_dashboard():
	return jsonify({'users': [user.__dict__ for user in users.values()], 'urls': [url.__dict__ for url in url_data.values()]}), 200

@app.route('/admin/delete_user', methods=['DELETE'])
def delete_user():
	data = request.get_json()
	username = data['username']
	if username not in users:
		return jsonify({'message': 'User not found'}), 404
	del users[username]
	return jsonify({'message': 'User deleted successfully'}), 200

@app.route('/admin/delete_url', methods=['DELETE'])
def delete_url():
	data = request.get_json()
	shortened_url = data['shortened_url']
	if shortened_url not in url_data:
		return jsonify({'message': 'URL not found'}), 404
	del url_data[shortened_url]
	return jsonify({'message': 'URL deleted successfully'}), 200
