from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
DB = {
	'users': {},
	'clubs': {},
	'books': {},
	'meetings': {},
	'discussions': {},
	'resources': {}
}

@dataclass
class User:
	id: str
	name: str
	email: str
	clubs: Dict[str, str]  # club_id: role
	books_read: Dict[str, str]  # book_id: status
	following: Dict[str, str]  # user_id: status

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: Dict[str, str]  # user_id: role
	books: Dict[str, str]  # book_id: status

@dataclass
class Book:
	id: str
	title: str
	author: str
	description: str

@dataclass
class Meeting:
	id: str
	club_id: str
	book_id: str
	schedule: str

@dataclass
class Discussion:
	id: str
	club_id: str
	book_id: str
	user_id: str
	message: str

@dataclass
class Resource:
	id: str
	title: str
	description: str
	link: str

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	user = DB['users'].get(id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user)

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	user = DB['users'].get(id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	data = request.get_json()
	user = User(**data)
	DB['users'][id] = user
	return jsonify(user)

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	user = DB['users'].get(id)
	if not user:
		return jsonify({'error': 'User not found'}), 404
	del DB['users'][id]
	return jsonify({'success': 'User deleted'}), 200

# Similar CRUD operations for Club, Book, Meeting, Discussion, Resource

if __name__ == '__main__':
	app.run(debug=True)
