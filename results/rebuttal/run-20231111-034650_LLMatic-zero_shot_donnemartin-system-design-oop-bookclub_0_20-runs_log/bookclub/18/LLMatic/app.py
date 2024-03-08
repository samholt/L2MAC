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
	email = data['email']
	password = data['password']
	if username in DATABASE['users']:
		return {'message': 'User already exists'}, 400
	DATABASE['users'][username] = {'email': email, 'password': password}
	DATABASE['user_profiles'][username] = {'read_books': [], 'wish_list': [], 'following': []}
	return {'message': 'User registered successfully'}, 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data['username']
	password = data['password']
	if username not in DATABASE['users'] or DATABASE['users'][username]['password'] != password:
		return {'message': 'Invalid username or password'}, 400
	return {'message': 'Logged in successfully'}, 200

@app.route('/view_profile', methods=['GET'])
def view_profile():
	username = request.args.get('username')
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	return DATABASE['user_profiles'][username], 200

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	username = data['username']
	new_data = data['new_data']
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	DATABASE['user_profiles'][username].update(new_data)
	return {'message': 'Profile updated successfully'}, 200

@app.route('/add_book', methods=['POST'])
def add_book():
	data = request.get_json()
	username = data['username']
	book_title = data['book_title']
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	DATABASE['user_profiles'][username]['read_books'].append(book_title)
	return {'message': 'Book added to read books successfully'}, 200

@app.route('/add_to_wish_list', methods=['POST'])
def add_to_wish_list():
	data = request.get_json()
	username = data['username']
	book_title = data['book_title']
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	DATABASE['user_profiles'][username]['wish_list'].append(book_title)
	return {'message': 'Book added to wish list successfully'}, 200

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	username = data['username']
	user_to_follow = data['user_to_follow']
	if username not in DATABASE['user_profiles'] or user_to_follow not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	DATABASE['user_profiles'][username]['following'].append(user_to_follow)
	return {'message': 'User followed successfully'}, 200

@app.route('/generate_recommendations', methods=['POST'])
def generate_recommendations():
	data = request.get_json()
	username = data['username']
	if username not in DATABASE['user_profiles']:
		return {'message': 'User does not exist'}, 400
	read_books = DATABASE['user_profiles'][username]['read_books']
	recommendations = []
	for user in DATABASE['user_profiles']:
		if user != username:
			for book in DATABASE['user_profiles'][user]['read_books']:
				if book not in read_books and book not in recommendations:
					recommendations.append(book)
	DATABASE['recommendations'][username] = recommendations
	return {'message': 'Recommendations generated successfully'}, 200

@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
	return DATABASE, 200

@app.route('/admin/remove_user', methods=['POST'])
def remove_user():
	data = request.get_json()
	username = data['username']
	if username not in DATABASE['users']:
		return {'message': 'User does not exist'}, 400
	del DATABASE['users'][username]
	del DATABASE['user_profiles'][username]
	return {'message': 'User removed successfully'}, 200

@app.route('/admin/remove_book', methods=['POST'])
def remove_book():
	data = request.get_json()
	book_title = data['book_title']
	for user in DATABASE['user_profiles']:
		if book_title in DATABASE['user_profiles'][user]['read_books']:
			DATABASE['user_profiles'][user]['read_books'].remove(book_title)
		if book_title in DATABASE['user_profiles'][user]['wish_list']:
			DATABASE['user_profiles'][user]['wish_list'].remove(book_title)
	return {'message': 'Book removed successfully'}, 200

@app.route('/notifications', methods=['POST'])
def notifications():
	data = request.get_json()
	username = data['username']
	notification = data['notification']
	if username not in DATABASE['users']:
		return {'message': 'User does not exist'}, 400
	if username not in DATABASE['notifications']:
		DATABASE['notifications'][username] = []
	DATABASE['notifications'][username].append(notification)
	return {'message': 'Notification added successfully'}, 200

@app.route('/view_notifications', methods=['GET'])
def view_notifications():
	username = request.args.get('username')
	if username not in DATABASE['notifications']:
		return {'message': 'No notifications for this user'}, 400
	return {'notifications': DATABASE['notifications'][username]}, 200

if __name__ == '__main__':
	app.run(debug=True)
