from flask import Flask, request, jsonify
from dataclasses import dataclass
import user

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	new_user = user.User(data['username'], data['password'])
	user.users[new_user.username] = new_user
	return jsonify(new_user.to_dict()), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	if username in user.users:
		return jsonify(user.users[username].to_dict()), 200
	else:
		return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
