from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
users = {}
bookclubs = {}
meetings = {}

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	users[data['id']] = data
	return jsonify(data), 201

@app.route('/join_bookclub', methods=['POST'])
def join_bookclub():
	data = request.get_json()
	bookclubs[data['id']] = data
	return jsonify(data), 201

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meetings[data['id']] = data
	return jsonify(data), 201

@app.route('/user/<user_id>', methods=['GET'])
def user_profile(user_id):
	user = users.get(user_id)
	if user is None:
		return jsonify({'error': 'User not found'}), 404
	return jsonify(user), 200

@app.route('/bookclub/<bookclub_id>', methods=['GET'])
def bookclub_page(bookclub_id):
	bookclub = bookclubs.get(bookclub_id)
	if bookclub is None:
		return jsonify({'error': 'Bookclub not found'}), 404
	return jsonify(bookclub), 200

@app.route('/meeting/<meeting_id>', methods=['GET'])
def meeting_page(meeting_id):
	meeting = meetings.get(meeting_id)
	if meeting is None:
		return jsonify({'error': 'Meeting not found'}), 404
	return jsonify(meeting), 200

if __name__ == '__main__':
	app.run()

