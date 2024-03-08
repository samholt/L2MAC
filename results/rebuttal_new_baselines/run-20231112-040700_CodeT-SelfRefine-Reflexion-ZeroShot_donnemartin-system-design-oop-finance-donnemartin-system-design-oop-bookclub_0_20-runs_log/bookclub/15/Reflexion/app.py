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
		if not club.is_private:
			club.members.append(user.name)
			user.clubs.append(club.name)
			return jsonify({'message': 'User joined the club successfully'}), 200
		else:
			return jsonify({'message': 'This club is private'}), 403
	else:
		return jsonify({'message': 'Club or user not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
