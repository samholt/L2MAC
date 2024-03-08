from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	name: str
	email: str
	books_read: list
	books_to_read: list
	clubs: list

@dataclass
class Club:
	name: str
	description: str
	is_private: bool
	members: list
	books: list

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.email] = user
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE[club.name] = club
	return jsonify(club), 201

if __name__ == '__main__':
	app.run(debug=True)
