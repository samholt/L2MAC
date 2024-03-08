from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

@dataclass
class User:
	id: str
	urls: Dict[str, str]

users = {}

@app.route('/user', methods=['POST'])
def create_user():
	user_id = request.json.get('id')
	if user_id in users:
		return jsonify({'error': 'User already exists'}), 400
	users[user_id] = User(id=user_id, urls={})
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	if user_id not in users:
		return jsonify({'error': 'User not found'}), 404
	del users[user_id]
	return jsonify({'message': 'User deleted'}), 200

@app.route('/user/<user_id>/url', methods=['POST'])
def shorten_url(user_id):
	if user_id not in users:
		return jsonify({'error': 'User not found'}), 404
	long_url = request.json.get('url')
	short_url = f'short.ly/{hash(long_url)}'
	users[user_id].urls[short_url] = long_url
	return jsonify({'short_url': short_url}), 201

if __name__ == '__main__':
	app.run(debug=True)
