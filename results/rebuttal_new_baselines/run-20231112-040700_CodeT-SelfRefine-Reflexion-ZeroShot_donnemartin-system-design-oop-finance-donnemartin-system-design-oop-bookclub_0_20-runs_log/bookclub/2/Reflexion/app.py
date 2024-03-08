from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'meetings': {},
	'books': {}
}

@dataclass
class User:
	id: str
	name: str
	email: str

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool

@dataclass
class Meeting:
	id: str
	club_id: str
	date: str

@dataclass
class Book:
	id: str
	title: str
	author: str

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return jsonify(dataclass_to_dict(user)), 201

@app.route('/clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'][club.id] = club
	return jsonify(dataclass_to_dict(club)), 201

@app.route('/meetings', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DATABASE['meetings'][meeting.id] = meeting
	return jsonify(dataclass_to_dict(meeting)), 201

@app.route('/books', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DATABASE['books'][book.id] = book
	return jsonify(dataclass_to_dict(book)), 201

if __name__ == '__main__':
	app.run(debug=True)
