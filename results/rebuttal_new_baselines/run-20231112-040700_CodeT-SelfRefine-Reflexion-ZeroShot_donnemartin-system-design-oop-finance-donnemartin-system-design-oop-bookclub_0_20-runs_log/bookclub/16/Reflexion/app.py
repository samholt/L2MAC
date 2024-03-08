from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
users = {}

@dataclass
class Club:
	name: str
description: str
is_private: bool
members: list

@dataclass
class User:
	name: str
clubs: list

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(data['name'], data['description'], data['is_private'], [])
	clubs[data['name']] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['name'], [])
	users[data['name']] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club = clubs.get(data['club_name'])
	user = users.get(data['user_name'])
	if club and user:
		club.members.append(user)
		user.clubs.append(club)
		return jsonify({'message': 'User joined club successfully'}), 200
	else:
		return jsonify({'message': 'Club or User not found'}), 404

@app.route('/list_clubs', methods=['GET'])
def list_clubs():
	return jsonify({'clubs': [club.name for club in clubs.values()]}), 200

@app.route('/list_user_clubs', methods=['GET'])
def list_user_clubs():
	user_name = request.args.get('user_name')
	user = users.get(user_name)
	if user:
		return jsonify({'clubs': [club.name for club in user.clubs]}), 200
	else:
		return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
