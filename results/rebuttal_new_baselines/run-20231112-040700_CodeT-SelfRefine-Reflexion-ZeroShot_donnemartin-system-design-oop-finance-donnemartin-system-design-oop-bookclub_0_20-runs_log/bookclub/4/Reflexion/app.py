from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'books': {},
	'meetings': {},
	'discussions': {},
	'recommendations': {}
}

@dataclass
class User:
	id: str
	name: str
	email: str
	books_read: list
	wish_list: list
	clubs_joined: list

@dataclass
class BookClub:
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
	time: str

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	user_id: str
	message: str
	replies: list

@dataclass
class Recommendation:
	id: str
	user_id: str
	book_id: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'][user.id] = user
	return jsonify(user), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
	user = DATABASE['users'].get(user_id)
	if user:
		return jsonify(user), 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/book_club', methods=['POST'])
def create_book_club():
	data = request.get_json()
	book_club = BookClub(**data)
	DATABASE['book_clubs'][book_club.id] = book_club
	return jsonify(book_club), 201

@app.route('/book_club/<club_id>', methods=['GET'])
def get_book_club(club_id):
	book_club = DATABASE['book_clubs'].get(club_id)
	if book_club:
		return jsonify(book_club), 200
	else:
		return {'message': 'Book club not found'}, 404

if __name__ == '__main__':
	app.run(debug=True)
