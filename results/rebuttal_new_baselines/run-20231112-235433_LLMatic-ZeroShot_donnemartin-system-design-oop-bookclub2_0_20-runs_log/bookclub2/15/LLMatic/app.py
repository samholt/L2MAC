from flask import Flask, request, jsonify
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion
from user import User
from admin import Admin

app = Flask(__name__)

admin = Admin()

@app.route('/book_club', methods=['POST'])
def book_club():
	data = request.get_json()
	club_name = data.get('club_name')
	privacy_setting = data.get('privacy_setting')
	response = admin.book_clubs.create_club(club_name, privacy_setting)
	return jsonify({'message': response}), 200

@app.route('/meeting', methods=['POST'])
def meeting():
	data = request.get_json()
	book_club_id = data.get('book_club_id')
	meeting_id = data.get('meeting_id')
	meeting_time = data.get('meeting_time')
	admin.meetings.schedule_meeting(book_club_id, meeting_id, meeting_time)
	return jsonify({'message': 'Meeting scheduled successfully'}), 200

@app.route('/discussion', methods=['POST'])
def discussion():
	data = request.get_json()
	forum_name = data.get('forum_name')
	admin.discussions.create_forum(forum_name)
	return jsonify({'message': 'Forum created successfully'}), 200

@app.route('/user', methods=['POST'])
def user():
	data = request.get_json()
	username = data.get('username')
	admin.create_user(username)
	return jsonify({'message': 'User created successfully'}), 200

@app.route('/admin', methods=['GET'])
def admin_route():
	analytics = admin.generate_analytics()
	return jsonify(analytics), 200

if __name__ == '__main__':
	app.run(debug=True)
