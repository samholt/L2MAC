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
	email: str
	clubs: list

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify(club), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users.get(data['user_name'])
	club = clubs.get(data['club_name'])
	if user is None or club is None:
		return jsonify({'message': 'User or club not found.'}), 404
	if not club.is_private:
		club.members.append(user.name)
		user.clubs.append(club.name)
		return jsonify(club), 200
	else:
		return jsonify({'message': 'This club is private.'}), 403

if __name__ == '__main__':
	app.run(debug=True)
