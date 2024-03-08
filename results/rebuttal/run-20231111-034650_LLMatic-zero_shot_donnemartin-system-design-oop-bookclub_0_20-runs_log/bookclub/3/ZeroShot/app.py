from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'books': {},
	'meetings': {},
	'discussions': {}
}

@dataclass
class User:
	id: str
	name: str
	email: str
	clubs: list
	books_read: list
	wish_list: list
	follows: list

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: list
	books: list
	meetings: list
	discussions: list

@dataclass
class Book:
	id: str
	title: str
	author: str
	summary: str
	reviews: list

@dataclass
class Meeting:
	id: str
	club_id: str
	book_id: str
	date: str
	reminder: bool

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	user_id: str
	message: str
	replies: list

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'][club.id] = club
	return jsonify(club), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DATABASE['books'][book.id] = book
	return jsonify(book), 201

@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DATABASE['meetings'][meeting.id] = meeting
	return jsonify(meeting), 201

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DATABASE['discussions'][discussion.id] = discussion
	return jsonify(discussion), 201

if __name__ == '__main__':
	app.run(debug=True)
