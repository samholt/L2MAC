from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
users = {}
clubs = {}

@dataclass
class User:
	name: str
	email: str
	clubs: list

@dataclass
class Club:
	name: str
	description: str
	members: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['name'], data['email'], [])
	users[data['email']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], [])
	clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users[data['email']]
	club = clubs[data['name']]
	user.clubs.append(club.name)
	club.members.append(user.email)
	return jsonify({'message': 'Joined club successfully'}), 200

@app.route('/list_clubs', methods=['GET'])
def list_clubs():
	return jsonify({'clubs': list(clubs.keys())}), 200

@app.route('/list_users', methods=['GET'])
def list_users():
	return jsonify({'users': list(users.keys())}), 200

if __name__ == '__main__':
	app.run(debug=True)
