from flask import Flask, request
from database import create_user, get_user, update_user, delete_user, create_club, get_club, update_club, delete_club, create_book, get_book, update_book, delete_book
from models import User, Club, Book

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user_route():
	data = request.get_json()
	user = User(**data)
	create_user(user)
	return {'message': 'User created'}, 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
	user = get_user(user_id)
	return user.__dict__, 200

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
	data = request.get_json()
	user = User(user_id, **data)
	update_user(user)
	return {'message': 'User updated'}, 200

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
	delete_user(user_id)
	return {'message': 'User deleted'}, 200

@app.route('/club', methods=['POST'])
def create_club_route():
	data = request.get_json()
	club = Club(**data)
	create_club(club)
	return {'message': 'Club created'}, 201

@app.route('/club/<int:club_id>', methods=['GET'])
def get_club_route(club_id):
	club = get_club(club_id)
	return club.__dict__, 200

@app.route('/club/<int:club_id>', methods=['PUT'])
def update_club_route(club_id):
	data = request.get_json()
	club = Club(club_id, **data)
	update_club(club)
	return {'message': 'Club updated'}, 200

@app.route('/club/<int:club_id>', methods=['DELETE'])
def delete_club_route(club_id):
	delete_club(club_id)
	return {'message': 'Club deleted'}, 200

@app.route('/book', methods=['POST'])
def create_book_route():
	data = request.get_json()
	book = Book(**data)
	create_book(book)
	return {'message': 'Book created'}, 201

@app.route('/book/<int:book_id>', methods=['GET'])
def get_book_route(book_id):
	book = get_book(book_id)
	return book.__dict__, 200

@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book_route(book_id):
	data = request.get_json()
	book = Book(book_id, **data)
	update_book(book)
	return {'message': 'Book updated'}, 200

@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book_route(book_id):
	delete_book(book_id)
	return {'message': 'Book deleted'}, 200

if __name__ == '__main__':
	app.run(debug=True)

