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
	'admin_actions': [],
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
	DATABASE['users'][username] = {'password': password}
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in DATABASE['users'] or DATABASE['users'][username]['password'] != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	if club_name in DATABASE['book_clubs']:
		return {'message': 'Book club already exists'}, 400
	DATABASE['book_clubs'][club_name] = {'members': [username]}
	return {'message': 'Book club created successfully'}, 200

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	club_name = data['club_name']
	username = data['username']
	if club_name not in DATABASE['book_clubs']:
		return {'message': 'Book club does not exist'}, 400
	if username in DATABASE['book_clubs'][club_name]['members']:
		return {'message': 'User is already a member of this book club'}, 400
	DATABASE['book_clubs'][club_name]['members'].append(username)
	return {'message': 'Joined book club successfully'}, 200

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	meeting_id = data['meeting_id']
	club_name = data['club_name']
	meeting_time = data['meeting_time']
	if meeting_id in DATABASE['meetings']:
		return {'message': 'Meeting already exists'}, 400
	DATABASE['meetings'][meeting_id] = {'club_name': club_name, 'meeting_time': meeting_time}
	return {'message': 'Meeting scheduled successfully'}, 200

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
	comment = data['comment']
	if discussion_id not in DATABASE['discussions']:
		return {'message': 'Discussion does not exist'}, 400
	DATABASE['discussions'][discussion_id]['comments'].append(comment)
	return {'message': 'Comment posted successfully'}, 200

@app.route('/suggest_book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	book_id = data['book_id']
	club_name = data['club_name']
	username = data['username']
	if book_id in DATABASE['book_selections']:
		return {'message': 'Book already suggested'}, 400
	DATABASE['book_selections'][book_id] = {'club_name': club_name, 'suggested_by': username, 'votes': 0}
	return {'message': 'Book suggested successfully'}, 200

@app.route('/vote_book', methods=['POST'])
def vote_book():
	data = request.get_json()
	book_id = data['book_id']
	if book_id not in DATABASE['book_selections']:
		return {'message': 'Book does not exist'}, 400
	DATABASE['book_selections'][book_id]['votes'] += 1
	return {'message': 'Vote counted successfully'}, 200

@app.route('/create_profile', methods=['POST'])
def create_profile():
	data = request.get_json()
	username = data['username']
	profile_info = data['profile_info']
	if username in DATABASE['user_profiles']:
		return {'message': 'Profile already exists'}, 400
	DATABASE['user_profiles'][username] = profile_info
	return {'message': 'Profile created successfully'}, 200

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	username = data['username']
	profile_info = data['profile_info']
	if username not in DATABASE['user_profiles']:
		return {'message': 'Profile does not exist'}, 400
	DATABASE['user_profiles'][username] = profile_info
	return {'message': 'Profile updated successfully'}, 200

@app.route('/view_profile', methods=['GET'])
def view_profile():
	username = request.args.get('username')
	if username not in DATABASE['user_profiles']:
		return {'message': 'Profile does not exist'}, 400
	return DATABASE['user_profiles'][username], 200

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	username = data['username']
	user_to_follow = data['user_to_follow']
	if username not in DATABASE['user_profiles'] or user_to_follow not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	if 'following' not in DATABASE['user_profiles'][username]:
		DATABASE['user_profiles'][username]['following'] = []
	DATABASE['user_profiles'][username]['following'].append(user_to_follow)
	return {'message': 'User followed successfully'}, 200

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
	data = request.get_json()
	username = data['username']
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	# For simplicity, we will recommend the top 5 most voted books
	recommended_books = sorted(DATABASE['book_selections'].items(), key=lambda x: x[1]['votes'], reverse=True)[:5]
	DATABASE['recommendations'][username] = [book[0] for book in recommended_books]
	return {'message': 'Recommendations generated successfully'}, 200

@app.route('/admin/manage_club', methods=['POST'])
def manage_club():
	data = request.get_json()
	club_name = data['club_name']
	action = data['action']
	if club_name not in DATABASE['book_clubs']:
		return {'message': 'Book club does not exist'}, 400
	if action == 'delete':
		del DATABASE['book_clubs'][club_name]
		DATABASE['admin_actions'].append({'action': 'deleted club', 'club_name': club_name})
		return {'message': 'Book club deleted successfully'}, 200
	elif action == 'add_member':
		username = data['username']
		if username in DATABASE['book_clubs'][club_name]['members']:
			return {'message': 'User is already a member of this book club'}, 400
		DATABASE['book_clubs'][club_name]['members'].append(username)
		DATABASE['admin_actions'].append({'action': 'added member to club', 'club_name': club_name, 'username': username})
		return {'message': 'Member added to book club successfully'}, 200
	elif action == 'remove_member':
		username = data['username']
		if username not in DATABASE['book_clubs'][club_name]['members']:
			return {'message': 'User is not a member of this book club'}, 400
		DATABASE['book_clubs'][club_name]['members'].remove(username)
		DATABASE['admin_actions'].append({'action': 'removed member from club', 'club_name': club_name, 'username': username})
		return {'message': 'Member removed from book club successfully'}, 200

@app.route('/admin/manage_user', methods=['POST'])
def manage_user():
	data = request.get_json()
	username = data['username']
	action = data['action']
	if username not in DATABASE['users']:
		return {'message': 'User does not exist'}, 400
	if action == 'delete':
		del DATABASE['users'][username]
		DATABASE['admin_actions'].append({'action': 'deleted user', 'username': username})
		return {'message': 'User deleted successfully'}, 200
	elif action == 'reset_password':
		new_password = data['new_password']
		DATABASE['users'][username]['password'] = new_password
		DATABASE['admin_actions'].append({'action': 'reset user password', 'username': username})
		return {'message': 'User password reset successfully'}, 200

@app.route('/admin/remove_content', methods=['POST'])
def remove_content():
	data = request.get_json()
	content_type = data['content_type']
	content_id = data['content_id']
	if content_type not in DATABASE or content_id not in DATABASE[content_type]:
		return {'message': 'Content does not exist'}, 400
	del DATABASE[content_type][content_id]
	DATABASE['admin_actions'].append({'action': 'removed content', 'content_type': content_type, 'content_id': content_id})
	return {'message': 'Content removed successfully'}, 200

@app.route('/admin/view_analytics', methods=['GET'])
def view_analytics():
	# For simplicity, we will return the count of users, book clubs, and discussions
	user_count = len(DATABASE['users'])
	book_club_count = len(DATABASE['book_clubs'])
	discussion_count = len(DATABASE['discussions'])
	return {'user_count': user_count, 'book_club_count': book_club_count, 'discussion_count': discussion_count}, 200

@app.route('/set_notification', methods=['POST'])
def set_notification():
	data = request.get_json()
	username = data['username']
	notification = data['notification']
	if username not in DATABASE['users']:
		return {'message': 'User does not exist'}, 400
	if 'notifications' not in DATABASE['users'][username]:
		DATABASE['users'][username]['notifications'] = []
	DATABASE['users'][username]['notifications'].append(notification)
	return {'message': 'Notification set successfully'}, 200

@app.route('/view_notifications', methods=['GET'])
def view_notifications():
	username = request.args.get('username')
	if username not in DATABASE['users'] or 'notifications' not in DATABASE['users'][username]:
		return {'message': 'No notifications found'}, 400
	return {'notifications': DATABASE['users'][username]['notifications']}, 200

if __name__ == '__main__':
	app.run(debug=True)
