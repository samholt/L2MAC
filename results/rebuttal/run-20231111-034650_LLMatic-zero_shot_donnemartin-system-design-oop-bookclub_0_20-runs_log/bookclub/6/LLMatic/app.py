from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'book_selections': {},
	'user_profiles': {},
	'recommendations': {},
	'admin_dashboard': {},
	'notifications': {},
	'resource_library': {}
}

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	if username in DATABASE['users']:
		return jsonify({'message': 'User already exists'}), 400
	DATABASE['users'][username] = {
		'password': data['password'],
		'email': data['email'],
		'book_clubs': []
	}
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	if username not in DATABASE['users'] or DATABASE['users'][username]['password'] != data['password']:
		return jsonify({'message': 'Invalid username or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data['club_name']
	if club_name in DATABASE['book_clubs']:
		return jsonify({'message': 'Book club already exists'}), 400
	DATABASE['book_clubs'][club_name] = {
		'description': data['description'],
		'is_public': data['is_public'],
		'admin': data['admin'],
		'members': [data['admin']]
	}
	DATABASE['users'][data['admin']]['book_clubs'].append(club_name)
	return jsonify({'message': 'Book club created successfully'}), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	if club_name not in DATABASE['book_clubs'] or username not in DATABASE['users']:
		return jsonify({'message': 'Invalid book club or user'}), 400
	if not DATABASE['book_clubs'][club_name]['is_public'] and DATABASE['book_clubs'][club_name]['admin'] != username:
		return jsonify({'message': 'Cannot join a private club without admin permission'}), 403
	DATABASE['book_clubs'][club_name]['members'].append(username)
	DATABASE['users'][username]['book_clubs'].append(club_name)
	return jsonify({'message': 'Joined the book club successfully'}), 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting_id = data['meeting_id']
	if meeting_id in DATABASE['meetings']:
		return jsonify({'message': 'Meeting already exists'}), 400
	DATABASE['meetings'][meeting_id] = {
		'date_time': data['date_time'],
		'book_club': data['book_club'],
		'attendees': data['attendees']
	}
	return jsonify({'message': 'Meeting scheduled successfully'}), 201

@app.route('/create_discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion_id = data['discussion_id']
	if discussion_id in DATABASE['discussions']:
		return jsonify({'message': 'Discussion already exists'}), 400
	DATABASE['discussions'][discussion_id] = {
		'title': data['title'],
		'book_club': data['book_club'],
		'comments': []
	}
	return jsonify({'message': 'Discussion created successfully'}), 201

@app.route('/post_comment', methods=['POST'])
def post_comment():
	data = request.get_json()
	discussion_id = data['discussion_id']
	if discussion_id not in DATABASE['discussions']:
		return jsonify({'message': 'Invalid discussion'}), 400
	comment = {
		'user': data['user'],
		'comment': data['comment'],
		'replies': []
	}
	DATABASE['discussions'][discussion_id]['comments'].append(comment)
	return jsonify({'message': 'Comment posted successfully'}), 201

@app.route('/post_reply', methods=['POST'])
def post_reply():
	data = request.get_json()
	discussion_id = data['discussion_id']
	comment_index = data['comment_index']
	if discussion_id not in DATABASE['discussions'] or comment_index >= len(DATABASE['discussions'][discussion_id]['comments']):
		return jsonify({'message': 'Invalid discussion or comment'}), 400
	reply = {
		'user': data['user'],
		'reply': data['reply']
	}
	DATABASE['discussions'][discussion_id]['comments'][comment_index]['replies'].append(reply)
	return jsonify({'message': 'Reply posted successfully'}), 201

@app.route('/suggest_book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	book_id = data['book_id']
	if book_id in DATABASE['book_selections']:
		return jsonify({'message': 'Book already suggested'}), 400
	DATABASE['book_selections'][book_id] = {
		'title': data['title'],
		'author': data['author'],
		'votes': 0
	}
	return jsonify({'message': 'Book suggested successfully'}), 201

@app.route('/vote_book', methods=['POST'])
def vote_book():
	data = request.get_json()
	book_id = data['book_id']
	if book_id not in DATABASE['book_selections']:
		return jsonify({'message': 'Invalid book'}), 400
	DATABASE['book_selections'][book_id]['votes'] += 1
	return jsonify({'message': 'Vote counted successfully'}), 200

@app.route('/recommend_book', methods=['POST'])
def recommend_book():
	data = request.get_json()
	username = data['username']
	book_id = data['book_id']
	reason = data['reason']
	if username not in DATABASE['users'] or book_id not in DATABASE['book_selections']:
		return jsonify({'message': 'Invalid user or book'}), 400
	DATABASE['recommendations'][username] = {
		'book_id': book_id,
		'reason': reason
	}
	return jsonify({'message': 'Book recommended successfully'}), 201

@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
	return jsonify(DATABASE), 200

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	notification_id = data['notification_id']
	if notification_id in DATABASE['notifications']:
		return jsonify({'message': 'Notification already exists'}), 400
	DATABASE['notifications'][notification_id] = {
		'type': data['type'],
		'user': data['user'],
		'content': data['content']
	}
	return jsonify({'message': 'Notification created successfully'}), 201

if __name__ == '__main__':
	app.run(debug=True)
