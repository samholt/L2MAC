from flask import Flask, request, jsonify
from database import MockDatabase
from user import User
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion
from admin import Admin

app = Flask(__name__)
db = MockDatabase()

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(data['username'], data['password'], data['email'])
	db.add_user(user)
	return jsonify({'message': 'User created'}), 201

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
	user = db.get_user(username)
	if user:
		return jsonify(user.__dict__), 200
	else:
		return jsonify({'message': 'User not found'}), 404

@app.route('/book_club', methods=['POST'])
def create_book_club():
	data = request.get_json()
	book_club = BookClub(data['name'], data['privacy_settings'], data['members'], data['administrators'])
	db.add_book_club(book_club)
	return jsonify({'message': 'Book club created'}), 201

@app.route('/book_club/<name>', methods=['GET'])
def get_book_club(name):
	book_club = db.get_book_club(name)
	if book_club:
		return jsonify(book_club.__dict__), 200
	else:
		return jsonify({'message': 'Book club not found'}), 404

@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(data['date'], data['time'], data['attendees'], data['reminders'])
	db.add_meeting(meeting)
	return jsonify({'message': 'Meeting scheduled'}), 201

@app.route('/meeting/<date>', methods=['GET'])
def get_meeting(date):
	meeting = db.get_meeting(date)
	if meeting:
		return jsonify(meeting.__dict__), 200
	else:
		return jsonify({'message': 'Meeting not found'}), 404

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(data['topic'])
	db.add_discussion(discussion)
	return jsonify({'message': 'Discussion created'}), 201

@app.route('/discussion/<topic>', methods=['GET'])
def get_discussion(topic):
	discussion = db.get_discussion(topic)
	if discussion:
		return jsonify(discussion.__dict__), 200
	else:
		return jsonify({'message': 'Discussion not found'}), 404

@app.route('/admin', methods=['POST'])
def create_admin():
	admin = Admin()
	db.add_admin(admin)
	return jsonify({'message': 'Admin created'}), 201

if __name__ == '__main__':
	app.run(port=5001, debug=True)
