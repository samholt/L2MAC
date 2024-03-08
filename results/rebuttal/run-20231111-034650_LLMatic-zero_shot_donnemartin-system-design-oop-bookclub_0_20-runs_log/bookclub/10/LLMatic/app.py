from flask import Flask, request

app = Flask(__name__)

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'books': {},
	'notifications': {},
	'votes': {}
}

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	# Get all users
	users = DATABASE['users']
	# Get all book clubs
	book_clubs = DATABASE['book_clubs']
	# Get all discussions
	discussions = DATABASE['discussions']
	# Get all books
	books = DATABASE['books']
	# Get all votes
	votes = DATABASE['votes']
	# Calculate user engagement
	user_engagement = sum([len(user['books']) for user in users.values()]) / len(users) if users else 0
	# Calculate popular books
	popular_books = sorted([(book_id, len(votes)) for book_id, votes in votes.items()], key=lambda x: x[1], reverse=True)[:5]
	return {
		'users': users,
		'book_clubs': book_clubs,
		'discussions': discussions,
		'books': books,
		'user_engagement': user_engagement,
		'popular_books': popular_books
	}

@app.route('/user', methods=['POST'])
def create_user():
	data = request.get_json()
	DATABASE['users'][data['id']] = data
	return {'message': 'User created successfully'}, 201

@app.route('/user/<id>', methods=['GET'])
def get_user(id):
	return DATABASE['users'].get(id, {})

@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
	data = request.get_json()
	DATABASE['users'][id].update(data)
	return {'message': 'User updated successfully'}

@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
	DATABASE['users'].pop(id, None)
	return {'message': 'User deleted successfully'}

@app.route('/bookclub', methods=['POST'])
def create_book_club():
	data = request.get_json()
	DATABASE['book_clubs'][data['id']] = data
	return {'message': 'Book club created successfully'}, 201

@app.route('/bookclub/<id>', methods=['GET'])
def get_book_club(id):
	return DATABASE['book_clubs'].get(id, {})

@app.route('/bookclub/<id>', methods=['PUT'])
def update_book_club(id):
	data = request.get_json()
	DATABASE['book_clubs'][id].update(data)
	return {'message': 'Book club updated successfully'}

@app.route('/bookclub/<id>', methods=['DELETE'])
def delete_book_club(id):
	DATABASE['book_clubs'].pop(id, None)
	return {'message': 'Book club deleted successfully'}

@app.route('/bookclub/<id>/join', methods=['POST'])
def join_book_club(id):
	user_id = request.get_json().get('user_id')
	if DATABASE['book_clubs'][id]['privacy'] == 'private' and user_id not in DATABASE['book_clubs'][id]['members']:
		return {'message': 'Request to join private book club sent'}
	DATABASE['book_clubs'][id]['members'].append(user_id)
	return {'message': 'Joined book club successfully'}

@app.route('/book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	DATABASE['books'][data['id']] = data
	return {'message': 'Book suggested successfully'}, 201

@app.route('/book/<id>', methods=['GET'])
def get_book(id):
	return DATABASE['books'].get(id, {})

@app.route('/book/<id>/vote', methods=['POST'])
def vote_book(id):
	user_id = request.get_json().get('user_id')
	DATABASE['votes'].setdefault(id, []).append(user_id)
	return {'message': 'Voted for book successfully'}

@app.route('/book/<id>/select', methods=['POST'])
def select_book(id):
	club_id = request.get_json().get('club_id')
	DATABASE['book_clubs'][club_id]['selected_book'] = id
	return {'message': 'Book selected for book club successfully'}

@app.route('/discussion', methods=['POST'])
def create_discussion():
	data = request.get_json()
	DATABASE['discussions'][data['id']] = data
	return {'message': 'Discussion created successfully'}, 201

@app.route('/discussion/<id>', methods=['GET'])
def get_discussion(id):
	return DATABASE['discussions'].get(id, {})

@app.route('/discussion/<id>', methods=['PUT'])
def update_discussion(id):
	data = request.get_json()
	DATABASE['discussions'][id].update(data)
	return {'message': 'Discussion updated successfully'}

@app.route('/discussion/<id>', methods=['DELETE'])
def delete_discussion(id):
	DATABASE['discussions'].pop(id, None)
	return {'message': 'Discussion deleted successfully'}

@app.route('/notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	DATABASE['notifications'][data['id']] = data
	return {'message': 'Notification created successfully'}, 201

@app.route('/notification/<id>', methods=['GET'])
def get_notification(id):
	return DATABASE['notifications'].get(id, {})

@app.route('/notification/<id>', methods=['PUT'])
def update_notification(id):
	data = request.get_json()
	DATABASE['notifications'][id].update(data)
	return {'message': 'Notification updated successfully'}

@app.route('/notification/<id>', methods=['DELETE'])
def delete_notification(id):
	DATABASE['notifications'].pop(id, None)
	return {'message': 'Notification deleted successfully'}

if __name__ == '__main__':
	app.run(debug=True)
