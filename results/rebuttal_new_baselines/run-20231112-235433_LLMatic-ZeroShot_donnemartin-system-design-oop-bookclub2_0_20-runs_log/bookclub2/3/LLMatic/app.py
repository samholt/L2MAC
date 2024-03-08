from flask import Flask, request, jsonify
from book_club import BookClub
from meeting import Meeting
from discussion import Discussion
from user import User
from admin import Admin

app = Flask(__name__)

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	if 'name' not in data or 'privacy' not in data or 'admin' not in data:
		return jsonify({'error': 'Missing required data'}), 400
	try:
		club = BookClub(data['name'], data['privacy'])
		club.create_club(data['admin'])
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'message': 'Club created'}), 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	if 'name' not in data or 'privacy' not in data or 'user' not in data:
		return jsonify({'error': 'Missing required data'}), 400
	try:
		club = BookClub(data['name'], data['privacy'])
		club.join_club(data['user'])
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'message': 'Joined club'}), 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	if 'club_id' not in data or 'meeting_time' not in data:
		return jsonify({'error': 'Missing required data'}), 400
	try:
		meeting = Meeting()
		meeting.schedule_meeting(data['club_id'], data['meeting_time'])
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'message': 'Meeting scheduled'}), 200

@app.route('/create_forum', methods=['POST'])
def create_forum():
	data = request.get_json()
	if 'club_id' not in data:
		return jsonify({'error': 'Missing required data'}), 400
	try:
		discussion = Discussion()
		discussion.create_forum(data['club_id'])
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'message': 'Forum created'}), 200

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	if 'username' not in data or 'password' not in data or 'profile' not in data:
		return jsonify({'error': 'Missing required data'}), 400
	try:
		user = User(data['username'], data['password'])
		user.create_profile(data['profile'])
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'message': 'User created'}), 200

@app.route('/access_dashboard', methods=['GET'])
def access_dashboard():
	try:
		admin = Admin()
		response = admin.access_dashboard()
	except Exception as e:
		return jsonify({'error': str(e)}), 500
	return jsonify({'dashboard': response}), 200

if __name__ == '__main__':
	app.run(debug=True)
