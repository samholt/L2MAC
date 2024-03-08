from flask import request, jsonify
from app import app, DB, User, Club, Book, Meeting, Discussion, Resource

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DB['clubs'][club.id] = club
	return jsonify(club), 201

@app.route('/book', methods=['POST'])
def create_book():
	data = request.get_json()
	book = Book(**data)
	DB['books'][book.id] = book
	return jsonify(book), 201

@app.route('/meeting', methods=['POST'])
def create_meeting():
	data = request.get_json()
	meeting = Meeting(**data)
	DB['meetings'][meeting.id] = meeting
	return jsonify(meeting), 201

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion = Discussion(**data)
	DB['discussions'][discussion.id] = discussion
	return jsonify(discussion), 201

@app.route('/resource', methods=['POST'])
def create_resource():
	data = request.get_json()
	resource = Resource(**data)
	DB['resources'][resource.id] = resource
	return jsonify(resource), 201
