from flask import Flask, request, jsonify
from dataclasses import dataclass, field

app = Flask(__name__)

clubs = {}
users = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: list = field(default_factory=list)

	def to_dict(self):
		return {'name': self.name, 'description': self.description, 'is_private': self.is_private}

@dataclass
class User:
	name: str
	email: str
	clubs: list = field(default_factory=list)

	def to_dict(self):
		return {'name': self.name, 'email': self.email, 'clubs': [club.to_dict() for club in self.clubs]}

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	if not all(key in data for key in ('name', 'description', 'is_private')):
		return jsonify({'message': 'Missing required field'}), 400
	club = Club(**data)
	clubs[club.name] = club
	return jsonify(club.to_dict()), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	if not all(key in data for key in ('user_name', 'club_name')):
		return jsonify({'message': 'Missing required field'}), 400
	user = users.get(data['user_name'])
	club = clubs.get(data['club_name'])
	if not user or not club:
		return jsonify({'message': 'User or club not found'}), 404
	if club.is_private:
		return jsonify({'message': 'This club is private'}), 403
	user.clubs.append(club)
	club.members.append(user)
	return jsonify(user.to_dict()), 200

if __name__ == '__main__':
	app.run(debug=True)
