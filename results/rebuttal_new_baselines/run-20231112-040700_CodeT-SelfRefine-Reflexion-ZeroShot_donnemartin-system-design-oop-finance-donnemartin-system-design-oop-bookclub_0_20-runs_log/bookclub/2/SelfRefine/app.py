from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
clubs = {}

@dataclass
class User:
	name: str
	email: str
	clubs: Dict[str, 'Club']

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: Dict[str, User]

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(name=data['name'], email=data['email'], clubs={})
	users[user.name] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(name=data['name'], description=data['description'], is_private=data['is_private'], members={})
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_name = data['user_name']
	club_name = data['club_name']
	if user_name not in users or club_name not in clubs:
		return jsonify({'message': 'User or club does not exist'}), 404
	club = clubs[club_name]
	if club.is_private:
		return jsonify({'message': 'Cannot join a private club'}), 403
	user = users[user_name]
	user.clubs[club.name] = club
	club.members[user.name] = user
	return jsonify({'message': 'User joined the club successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
