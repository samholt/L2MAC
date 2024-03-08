from flask import Flask, request
from models import User, Book, Admin, Notification, Resource

app = Flask(__name__)

# Mock database
app.users = {'test_user': User('test_user', 'test@test.com', 'password', [], [], [])}
app.books = {}
app.admins = {}
app.notifications = {}
app.resources = {}

@app.route('/view_profile', methods=['GET'])
def view_profile():
	data = request.get_json()
	user = app.users[data['username']]
	return {'user': user.to_dict()}, 200

@app.route('/edit_profile', methods=['PUT'])
def edit_profile():
	data = request.get_json()
	user = app.users[data['username']]
	user.reading_interests = data.get('reading_interests', user.reading_interests)
	user.read_books = data.get('read_books', user.read_books)
	user.wish_to_read_books = data.get('wish_to_read_books', user.wish_to_read_books)
	return {'message': 'Profile updated successfully'}, 200

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	user = app.users[data['username']]
	user_to_follow = app.users[data['user_to_follow']]
	user.follow(user_to_follow)
	return {'message': 'User followed successfully'}, 200

@app.route('/unfollow_user', methods=['POST'])
def unfollow_user():
	data = request.get_json()
	user = app.users[data['username']]
	user_to_unfollow = app.users[data['user_to_unfollow']]
	user.unfollow(user_to_unfollow)
	return {'message': 'User unfollowed successfully'}, 200

@app.route('/fetch_book_info', methods=['GET'])
def fetch_book_info():
	data = request.get_json()
	book = app.books[data['title']]
	return {'book': book.__dict__}, 200

@app.route('/recommend_books', methods=['GET'])
def recommend_books():
	data = request.get_json()
	user = app.users[data['username']]
	recommendations = user.recommend_books(app.books)
	return {'recommendations': [book.title for book in recommendations]}, 200

@app.route('/admin/manage_users', methods=['GET'])
def manage_users():
	data = request.get_json()
	admin = app.admins[data['username']]
	return {'users': admin.manage_users(app.users)}, 200

@app.route('/admin/manage_books', methods=['GET'])
def manage_books():
	data = request.get_json()
	admin = app.admins[data['username']]
	return {'books': admin.manage_books(app.books)}, 200

@app.route('/admin/remove_user', methods=['DELETE'])
def remove_user():
	data = request.get_json()
	admin = app.admins[data['username']]
	message = admin.remove_user(app.users, data['user_to_remove'])
	return {'message': message}, 200

@app.route('/admin/remove_book', methods=['DELETE'])
def remove_book():
	data = request.get_json()
	admin = app.admins[data['username']]
	message = admin.remove_book(app.books, data['book_to_remove'])
	return {'message': message}, 200

@app.route('/admin/view_analytics', methods=['GET'])
def view_analytics():
	data = request.get_json()
	admin = app.admins[data['username']]
	analytics = admin.view_analytics(app.users)
	return {'analytics': analytics}, 200

@app.route('/view_notifications', methods=['GET'])
def view_notifications():
	data = request.get_json()
	user = app.users[data['username']]
	return {'notifications': [notification.to_dict() for notification in user.notifications]}, 200

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	user = app.users[data['username']]
	notification = Notification(data['content'], user.username, data['date'])
	user.notifications.append(notification)
	app.notifications[notification.content] = notification
	return {'message': 'Notification created successfully'}, 200

@app.route('/view_resources', methods=['GET'])
def view_resources():
	return {'resources': [resource.to_dict() for resource in app.resources.values()]}, 200

@app.route('/contribute_resource', methods=['POST'])
def contribute_resource():
	data = request.get_json()
	resource = Resource(data['title'], data['content'], data['author'])
	app.resources[resource.title] = resource
	return {'message': 'Resource contributed successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
