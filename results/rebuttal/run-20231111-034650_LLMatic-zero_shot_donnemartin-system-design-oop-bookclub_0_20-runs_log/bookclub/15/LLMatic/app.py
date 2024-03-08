from flask import Flask, jsonify, request, session

app = Flask(__name__)
app.secret_key = 'secret'

# Mock database
DATABASE = {
	'users': {'admin': 'admin'},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'book_selections': {},
	'user_profiles': {'admin': {'username': 'admin', 'following': []}},
	'recommendations': {},
	'admin_actions': {},
	'notifications': {},
	'resources': {}
}

@app.route('/')
def home():
	return jsonify({'message': 'Welcome to the Book Club App!'}), 200

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if username in DATABASE['users']:
		return jsonify({'message': 'User already exists'}), 400
	DATABASE['users'][username] = password
	DATABASE['user_profiles'][username] = {'username': username, 'following': []}
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	if DATABASE['users'].get(username) != password:
		return jsonify({'message': 'Invalid username or password'}), 400
	session['username'] = username
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/profile/<username>', methods=['GET'])
def view_profile(username):
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	return jsonify(DATABASE['user_profiles'][username]), 200

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	DATABASE['user_profiles'][username].update(data)
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/books', methods=['GET'])
def list_books():
	return jsonify(list(DATABASE['book_selections'].keys())), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	username_to_follow = data.get('username')
	if username_to_follow not in DATABASE['user_profiles']:
		return jsonify({'message': 'User to follow does not exist'}), 400
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	if username_to_follow in DATABASE['user_profiles'][username]['following']:
		return jsonify({'message': 'Already following this user'}), 400
	DATABASE['user_profiles'][username]['following'].append(username_to_follow)
	return jsonify({'message': 'User followed successfully'}), 200

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	# Mock recommendation engine
	recommendations = ['Book1', 'Book2', 'Book3']
	return jsonify({'recommendations': recommendations}), 200

@app.route('/popular_books', methods=['GET'])
def get_popular_books():
	# Mock popular books
	popular_books = ['Book1', 'Book2', 'Book3']
	return jsonify({'popular_books': popular_books}), 200

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	# Check if the user is an admin
	username = session.get('username')
	if username not in DATABASE['users'] or DATABASE['users'][username] != 'admin':
		return jsonify({'message': 'Unauthorized'}), 403
	# Return all data in the database
	return jsonify(DATABASE), 200

@app.route('/notifications', methods=['POST'])
def set_notifications():
	data = request.get_json()
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	DATABASE['notifications'][username] = data.get('notifications')
	return jsonify({'message': 'Notifications set successfully'}), 200

@app.route('/notifications', methods=['GET'])
def get_notifications():
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	return jsonify(DATABASE['notifications'].get(username, {})), 200

@app.route('/resources', methods=['POST'])
def share_resources():
	data = request.get_json()
	username = session.get('username')
	if username not in DATABASE['user_profiles']:
		return jsonify({'message': 'User does not exist'}), 400
	DATABASE['resources'][username] = data.get('resources')
	return jsonify({'message': 'Resources shared successfully'}), 200

@app.route('/resources', methods=['GET'])
def view_resources():
	return jsonify(DATABASE['resources']), 200

if __name__ == '__main__':
	app.run(debug=True)
