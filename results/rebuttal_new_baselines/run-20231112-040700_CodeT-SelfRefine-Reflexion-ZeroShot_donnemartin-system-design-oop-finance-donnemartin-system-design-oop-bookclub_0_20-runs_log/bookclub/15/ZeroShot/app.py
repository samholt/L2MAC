from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
clubs = {}
users = {}

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: Dict

@dataclass
class User:
	name: str
	clubs: Dict

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.name] = club
	return jsonify({'message': 'Club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_name = data['user_name']
	club_name = data['club_name']
	if club_name in clubs and not clubs[club_name].is_private:
		clubs[club_name].members[user_name] = users[user_name]
		users[user_name].clubs[club_name] = clubs[club_name]
		return jsonify({'message': 'Joined club successfully'}), 200
	else:
		return jsonify({'message': 'Club does not exist or is private'}), 400

if __name__ == '__main__':
	app.run(debug=True)
