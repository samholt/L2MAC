from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'clubs': {},
	'books': {},
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

@dataclass
class Club:
	id: str
	name: str
	description: str
	members: list
	books: list
	meetings: list

@dataclass
class Book:
	id: str
	title: str
	author: str
	description: str

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	comments: list

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

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DATABASE['discussions'][discussion.id] = discussion
	return jsonify(discussion), 201

if __name__ == '__main__':
	app.run(debug=True)
