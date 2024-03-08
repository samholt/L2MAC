from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'

# Mock database
DATABASE = {
	'users': {},
	'book_clubs': {},
	'meetings': {},
	'discussions': {},
	'books': {},
	'notifications': {},
	'profiles': {},
	'resources': {}
}

@app.route('/')
def home():
	return 'Welcome to the Book Club App!'

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	
	if username in DATABASE['users']:
		return 'Username already exists', 400
	
	DATABASE['users'][username] = {
		'email': email,
		'password': generate_password_hash(password)
	}
	
	return 'User registered successfully', 200

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	
	if username not in DATABASE['users'] or not check_password_hash(DATABASE['users'][username]['password'], password):
		return 'Invalid username or password', 400
	
	session['username'] = username
	return 'Logged in successfully', 200

@app.route('/create_profile', methods=['POST'])
def create_profile():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	reading_interests = request.form['reading_interests']
	books_read = request.form['books_read']
	books_to_read = request.form['books_to_read']
	
	if username in DATABASE['profiles']:
		return 'Profile already exists', 400
	
	DATABASE['profiles'][username] = {
		'reading_interests': reading_interests,
		'books_read': books_read,
		'books_to_read': books_to_read,
		'following': []
	}
	
	return 'Profile created successfully', 200

@app.route('/update_profile', methods=['POST'])
def update_profile():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	reading_interests = request.form['reading_interests']
	books_read = request.form['books_read']
	books_to_read = request.form['books_to_read']
	
	if username not in DATABASE['profiles']:
		return 'Profile does not exist', 400
	
	DATABASE['profiles'][username]['reading_interests'] = reading_interests
	DATABASE['profiles'][username]['books_read'] = books_read
	DATABASE['profiles'][username]['books_to_read'] = books_to_read
	
	return 'Profile updated successfully', 200

@app.route('/view_profile', methods=['GET'])
def view_profile():
	username = request.args.get('username')
	
	if username not in DATABASE['profiles']:
		return 'Profile does not exist', 400
	
	return DATABASE['profiles'][username], 200

@app.route('/follow_user', methods=['POST'])
def follow_user():
	username_to_follow = request.form['username_to_follow']
	
	if username_to_follow not in DATABASE['profiles']:
		return 'User to follow does not exist', 400
	
	DATABASE['profiles'][session['username']]['following'].append(username_to_follow)
	
	return 'User followed successfully', 200

@app.route('/recommend_books', methods=['GET'])
def recommend_books():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	if username not in DATABASE['profiles']:
		return 'User does not exist', 400
	
	# Get the user's reading interests
	reading_interests = DATABASE['profiles'][username]['reading_interests']
	
	# Get the books read by the user
	books_read = DATABASE['profiles'][username]['books_read']
	
	# Get the books to read by the user
	books_to_read = DATABASE['profiles'][username]['books_to_read']
	
	# Get the books read by the community
	community_books = [book for user in DATABASE['profiles'].values() for book in user['books_read']]
	
	# Recommend books based on the user's reading interests and popular books within the community
	recommended_books = [book for book in community_books if book not in books_read and book not in books_to_read and book in reading_interests]
	
	return {'recommended_books': recommended_books}, 200

@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard():
	# Only allow admin to access this route
	if session.get('username') != 'admin':
		return 'Unauthorized', 403
	
	# Get analytics on user engagement and popular books
	user_engagement = {username: len(profile['books_read']) for username, profile in DATABASE['profiles'].items()}
	popular_books = {book: sum([profile['books_read'].count(book) for profile in DATABASE['profiles'].values()]) for book in DATABASE['books']}
	
	return {'user_engagement': user_engagement, 'popular_books': popular_books}, 200

@app.route('/manage_users', methods=['POST'])
def manage_users():
	# Only allow admin to access this route
	if session.get('username') != 'admin':
		return 'Unauthorized', 403
	
	action = request.form['action']
	username = request.form['username']
	
	if action == 'delete':
		if username in DATABASE['users']:
			del DATABASE['users'][username]
			return 'User deleted successfully', 200
		else:
			return 'User does not exist', 400
	elif action == 'suspend':
		if username in DATABASE['users']:
			DATABASE['users'][username]['suspended'] = True
			return 'User suspended successfully', 200
		else:
			return 'User does not exist', 400
	else:
		return 'Invalid action', 400

@app.route('/manage_book_clubs', methods=['POST'])
def manage_book_clubs():
	# Only allow admin to access this route
	if session.get('username') != 'admin':
		return 'Unauthorized', 403
	
	action = request.form['action']
	book_club_id = request.form['book_club_id']
	
	if action == 'delete':
		if book_club_id in DATABASE['book_clubs']:
			del DATABASE['book_clubs'][book_club_id]
			return 'Book club deleted successfully', 200
		else:
			return 'Book club does not exist', 400
	else:
		return 'Invalid action', 400

@app.route('/create_notification', methods=['POST'])
def create_notification():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	
	message = request.form['message']
	
	DATABASE['notifications'][username] = message
	
	return 'Notification created successfully', 200

@app.route('/view_notifications', methods=['GET'])
def view_notifications():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	
	return DATABASE['notifications'].get(username, 'No notifications'), 200

@app.route('/add_resource', methods=['POST'])
def add_resource():
	username = session.get('username')
	if not username:
		return 'User not logged in', 400
	
	resource = request.form['resource']
	
	DATABASE['resources'][username] = resource
	
	return 'Resource added successfully', 200

@app.route('/view_resources', methods=['GET'])
def view_resources():
	return DATABASE['resources'], 200

if __name__ == '__main__':
	app.run(debug=True)
