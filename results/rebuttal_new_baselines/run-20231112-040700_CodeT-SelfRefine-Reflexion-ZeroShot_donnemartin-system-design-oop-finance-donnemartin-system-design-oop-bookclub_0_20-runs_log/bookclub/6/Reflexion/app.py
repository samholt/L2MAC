from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

clubs = {}
books = {}
users = {}

@dataclass
class Book:
	id: str
	title: str
	author: str
	clubs: list

@dataclass
class Club:
	id: str
	name: str
	description: str
	books: list
	members: list

@dataclass
class User:
	id: str
	name: str
	clubs: list
	books: list

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.id] = club
	return jsonify(club), 201

@app.route('/club/<club_id>/add_book', methods=['POST'])
def add_book_to_club(club_id):
	data = request.get_json()
	book = Book(**data)
	books[book.id] = book
	clubs[club_id].books.append(book.id)
	book.clubs.append(club_id)
	return jsonify(book), 201

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return jsonify(user), 201

if __name__ == '__main__':
	app.run(debug=True)
