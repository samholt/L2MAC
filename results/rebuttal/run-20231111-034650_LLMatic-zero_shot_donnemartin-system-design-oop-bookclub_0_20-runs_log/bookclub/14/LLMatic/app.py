from flask import Flask, request, jsonify
from models.user import User
from models.book_club import BookClub
from models.meeting import Meeting
from models.discussion import Discussion
from models.book import Book
from models.notification import Notification

app = Flask(__name__)

users = {}
book_clubs = {}
meetings = {}
discussions = {}
books = {}
notifications = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User.create(data['name'], data['email'], data['password'])
	users[user.id] = user
	return jsonify({'message': 'User registered successfully', 'id': user.id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.authenticate(data['email'], data['password']):
			return jsonify({'message': 'Login successful', 'id': user.id}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/book_clubs', methods=['POST'])
def create_club():
	data = request.get_json()
	club = BookClub(None, data['name'], data['description'], data['privacy'], [], None)
	book_clubs[club.id] = club
	return jsonify({'message': 'Book club created successfully', 'id': club.id}), 201

@app.route('/meetings', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting = Meeting(None, data['date'], data['time'], book_clubs[data['book_club_id']])
	meetings[meeting.id] = meeting
	return jsonify({'message': 'Meeting scheduled successfully', 'id': meeting.id}), 201

@app.route('/discussions', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion.create_discussion(None, data['topic'], book_clubs[data['book_club_id']])
	discussions[discussion.id] = discussion
	return jsonify({'message': 'Discussion created successfully', 'id': discussion.id}), 201

@app.route('/books', methods=['POST'])
def add_book():
	data = request.get_json()
	book = Book.add_book(None, data['title'], data['author'])
	books[book.id] = book
	return jsonify({'message': 'Book added successfully', 'id': book.id}), 201

@app.route('/notifications', methods=['POST'])
def create_notification():
	data = request.get_json()
	notification = Notification(None, users[data['user_id']], data['message'])
	notifications[notification.id] = notification
	return jsonify({'message': 'Notification created successfully', 'id': notification.id}), 201

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users), 200

@app.route('/book_clubs', methods=['GET'])
def get_book_clubs():
	return jsonify(book_clubs), 200

@app.route('/meetings', methods=['GET'])
def get_meetings():
	return jsonify(meetings), 200

@app.route('/discussions', methods=['GET'])
def get_discussions():
	return jsonify(discussions), 200

@app.route('/books', methods=['GET'])
def get_books():
	return jsonify(books), 200

@app.route('/notifications', methods=['GET'])
def get_notifications():
	return jsonify(notifications), 200

if __name__ == '__main__':
	app.run()

