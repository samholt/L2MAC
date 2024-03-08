from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	id: int
	name: str
	email: str
	clubs: list
	books: list

@dataclass
class Club:
	id: int
	name: str
	description: str
	is_private: bool
	members: list
	books: list

@dataclass
class Book:
	id: int
	title: str
	author: str
	description: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE['users'].append(user)
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE['clubs'].append(club)
	return jsonify(club), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DATABASE['books'].append(book)
	return jsonify(book), 201

if __name__ == '__main__':
	app.run(debug=True)
