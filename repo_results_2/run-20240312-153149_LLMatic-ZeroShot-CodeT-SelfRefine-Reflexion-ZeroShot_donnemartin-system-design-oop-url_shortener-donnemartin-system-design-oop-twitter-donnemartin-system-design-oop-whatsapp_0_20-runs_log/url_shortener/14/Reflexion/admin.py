from flask import Flask, request, jsonify
from database import users, urls, delete_user, delete_url


app = Flask(__name__)


@app.route('/admin/users', methods=['GET'])
def get_all_users():
	return jsonify(users), 200


@app.route('/admin/urls', methods=['GET'])
def get_all_urls():
	return jsonify(urls), 200


@app.route('/admin/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
	delete_user(user_id)
	return jsonify({'message': 'User deleted successfully'}), 200


@app.route('/admin/urls/<url_id>', methods=['DELETE'])
def remove_url(url_id):
	delete_url(url_id)
	return jsonify({'message': 'URL deleted successfully'}), 200

