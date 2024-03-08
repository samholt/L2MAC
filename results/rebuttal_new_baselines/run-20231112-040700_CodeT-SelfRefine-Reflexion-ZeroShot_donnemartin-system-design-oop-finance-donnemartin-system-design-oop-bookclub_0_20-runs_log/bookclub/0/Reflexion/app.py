from flask import Flask, request
from database import users, clubs, books, meetings, reviews
from models import User, Club, Book, Meeting, Review

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	users[user.id] = user
	return {'id': user.id}, 201

@app.route('/clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	clubs[club.id] = club
	return {'id': club.id}, 201

@app.route('/books', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	books[book.id] = book
	return {'id': book.id}, 201

@app.route('/meetings', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	meetings[meeting.id] = meeting
	return {'id': meeting.id}, 201

@app.route('/reviews', methods=['POST'])
def create_review():
	data = request.get_json()
	review = Review(**data)
	reviews[review.id] = review
	return {'id': review.id}, 201

if __name__ == '__main__':
	app.run(debug=True)

