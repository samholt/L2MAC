from flask import Flask, request

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
	'admin_actions': {},
	'notifications': {},
	'resources': {}
}

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username in DATABASE['users']:
		return {'message': 'User already exists'}, 400
	DATABASE['users'][username] = password
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in DATABASE['users'] or DATABASE['users'][username] != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	if club_name in DATABASE['book_clubs']:
		return {'message': 'Book club already exists'}, 400
	DATABASE['book_clubs'][club_name] = {'creator': username, 'members': [username]}
	return {'message': 'Book club created successfully'}, 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	if club_name not in DATABASE['book_clubs']:
		return {'message': 'Book club does not exist'}, 400
	if username in DATABASE['book_clubs'][club_name]['members']:
		return {'message': 'User is already a member of the book club'}, 400
	DATABASE['book_clubs'][club_name]['members'].append(username)
	return {'message': 'Joined book club successfully'}, 200

@app.route('/manage_club', methods=['POST'])
def manage_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	action = data['action']
	if club_name not in DATABASE['book_clubs']:
		return {'message': 'Book club does not exist'}, 400
	if action == 'remove' and username in DATABASE['book_clubs'][club_name]['members']:
		DATABASE['book_clubs'][club_name]['members'].remove(username)
		return {'message': 'Member removed successfully'}, 200
	return {'message': 'Invalid action'}, 400

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting_id = data['meeting_id']
	club_name = data['club_name']
	meeting_details = data['meeting_details']
	if meeting_id in DATABASE['meetings']:
		return {'message': 'Meeting already scheduled'}, 400
	DATABASE['meetings'][meeting_id] = {'club_name': club_name, 'details': meeting_details}
	return {'message': 'Meeting scheduled successfully'}, 200

@app.route('/send_reminder', methods=['POST'])
def send_reminder():
	data = request.get_json()
	meeting_id = data['meeting_id']
	reminder = data['reminder']
	if meeting_id not in DATABASE['meetings']:
		return {'message': 'Meeting does not exist'}, 400
	DATABASE['notifications'][meeting_id] = reminder
	return {'message': 'Reminder sent successfully'}, 200

@app.route('/create_discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	discussion_id = data['discussion_id']
	club_name = data['club_name']
	topic = data['topic']
	if discussion_id in DATABASE['discussions']:
		return {'message': 'Discussion already exists'}, 400
	DATABASE['discussions'][discussion_id] = {'club_name': club_name, 'topic': topic, 'comments': []}
	return {'message': 'Discussion created successfully'}, 200

@app.route('/post_comment', methods=['POST'])
def post_comment():
	data = request.get_json()
	discussion_id = data['discussion_id']
	username = data['username']
	comment = data['comment']
	if discussion_id not in DATABASE['discussions']:
		return {'message': 'Discussion does not exist'}, 400
	DATABASE['discussions'][discussion_id]['comments'].append({'username': username, 'comment': comment})
	return {'message': 'Comment posted successfully'}, 200

@app.route('/suggest_book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	book_id = data['book_id']
	if club_name not in DATABASE['book_clubs']:
		return {'message': 'Book club does not exist'}, 400
	if username not in DATABASE['book_clubs'][club_name]['members']:
		return {'message': 'User is not a member of the book club'}, 400
	DATABASE['book_selections'][book_id] = {'club_name': club_name, 'suggester': username, 'votes': 0}
	return {'message': 'Book suggested successfully'}, 200

@app.route('/vote_book', methods=['POST'])
def vote_book():
	data = request.get_json()
	book_id = data['book_id']
	username = data['username']
	if book_id not in DATABASE['book_selections']:
		return {'message': 'Book does not exist'}, 400
	DATABASE['book_selections'][book_id]['votes'] += 1
	return {'message': 'Vote casted successfully'}, 200

@app.route('/recommend_books', methods=['POST'])
def recommend_books():
	data = request.get_json()
	username = data['username']
	if username not in DATABASE['users']:
		return {'message': 'User does not exist'}, 400
	user_reading_history = DATABASE['user_profiles'][username]['reading_history']
	user_genres = [book['genre'] for book in user_reading_history]
	most_common_genres = [genre for genre in set(user_genres) if user_genres.count(genre) > 1]
	recommendations = [book for book in DATABASE['book_selections'].values() if book['genre'] in most_common_genres and book not in user_reading_history]
	return {'recommendations': recommendations}, 200

if __name__ == '__main__':
	app.run(debug=True)
