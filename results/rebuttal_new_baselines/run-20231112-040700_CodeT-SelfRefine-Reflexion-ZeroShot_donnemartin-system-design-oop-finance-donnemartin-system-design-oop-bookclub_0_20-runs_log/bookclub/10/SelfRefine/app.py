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

	def __init__(self, name, description, is_private, members):
		self.name = name
		self.description = description
		self.is_private = is_private
		self.members = members

@dataclass
class User:
	name: str
	email: str
	clubs: list

	def __init__(self, name, email, clubs):
		self.name = name
		self.email = email
		self.clubs = clubs

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.name] = user
	return jsonify({'message': 'User created successfully'}), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user = users.get(data['user_name'])
	club = clubs.get(data['club_name'])
	if user and club:
		if not club.is_private:
			club.members.append(user)
			user.clubs.append(club)
			return jsonify({'message': 'Joined club successfully'}), 200
		else:
			return jsonify({'message': 'This club is private'}), 403
	else:
		return jsonify({'message': 'User or club not found'}), 404

if __name__ == '__main__':
	app.run(debug=True)
