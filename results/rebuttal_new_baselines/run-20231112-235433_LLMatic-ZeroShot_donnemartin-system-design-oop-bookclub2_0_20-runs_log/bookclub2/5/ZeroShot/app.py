from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
clubs = {}
meetings = {}
discussions = {}


@dataclass
class User:
	id: str
	name: str
	clubs: Dict[str, 'Club']
	
	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'clubs': {club_id: club.to_dict() for club_id, club in self.clubs.items()}
		}


@dataclass
class Club:
	id: str
	name: str
	creator: User
	members: Dict[str, User]
	
	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'creator': self.creator.id,
			'members': [user.id for user in self.members.values()]
		}


@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(id=data['id'], name=data['name'], clubs={})
	users[user.id] = user
	return jsonify(user.to_dict()), 201


@app.route('/clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	creator = users[data['creator']]
	club = Club(id=data['id'], name=data['name'], creator=creator, members={creator.id: creator})
	clubs[club.id] = club
	creator.clubs[club.id] = club
	return jsonify(club.to_dict()), 201


if __name__ == '__main__':
	app.run(debug=True)
