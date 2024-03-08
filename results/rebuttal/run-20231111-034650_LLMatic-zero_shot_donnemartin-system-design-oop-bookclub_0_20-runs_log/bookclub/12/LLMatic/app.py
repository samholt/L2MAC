from flask import Flask, request
from models import User, BookClub, Meeting, DiscussionForum, Book, Notification, Resource

app = Flask(__name__)

# Mock database
users = {}
bookclubs = {}
meetings = {}
discussion_forums = {}
books = {}
notifications = {}
resources = {}

@app.route('/')
def home():
	return 'Hello, BookClub!'

@app.route('/create_bookclub', methods=['POST'])
def create_bookclub():
	data = request.get_json()
	bookclub = BookClub(data['name'], data['description'], data['is_private'])
	bookclubs[data['name']] = bookclub
	return 'BookClub created successfully', 201

@app.route('/join_bookclub', methods=['POST'])
def join_bookclub():
	data = request.get_json()
	user = users.get(data['username'])
	bookclub = bookclubs.get(data['bookclub_name'])
	if user and bookclub:
		bookclub.members.append(user)
		return 'Joined BookClub successfully', 200
	else:
		return 'User or BookClub not found', 404

@app.route('/schedule_meeting', methods=['POST'])
def schedule_meeting():
	data = request.get_json()
	bookclub = bookclubs.get(data['bookclub_name'])
	if bookclub:
		meeting = Meeting(data['date'], data['time'], data['attendees'], bookclub)
		bookclub.meetings.append(meeting)
		meetings[data['date']] = meeting
		return 'Meeting scheduled successfully', 201
	else:
		return 'BookClub not found', 404

@app.route('/view_meetings', methods=['GET'])
def view_meetings():
	return {date: {'date': meeting.date, 'time': meeting.time, 'attendees': meeting.attendees} for date, meeting in meetings.items()}, 200

@app.route('/export_meeting', methods=['GET'])
def export_meeting():
	date = request.args.get('date')
	meeting = meetings.get(date)
	if meeting:
		return meeting.to_ical(), 200
	else:
		return 'Meeting not found', 404

@app.route('/create_forum', methods=['POST'])
def create_forum():
	data = request.get_json()
	bookclub = bookclubs.get(data['bookclub_name'])
	if bookclub:
		forum = DiscussionForum(data['topic'], bookclub)
		bookclub.discussion_forums.append(forum)
		discussion_forums[data['topic']] = forum
		return 'Forum created successfully', 201
	else:
		return 'BookClub not found', 404

@app.route('/post_in_forum', methods=['POST'])
def post_in_forum():
	data = request.get_json()
	forum = discussion_forums.get(data['topic'])
	if forum:
		forum.posts.append(data['post'])
		return 'Post added successfully', 201
	else:
		return 'Forum not found', 404

@app.route('/view_forum_posts', methods=['GET'])
def view_forum_posts():
	topic = request.args.get('topic')
	forum = discussion_forums.get(topic)
	if forum:
		return {'posts': forum.posts}, 200
	else:
		return 'Forum not found', 404

@app.route('/suggest_book', methods=['POST'])
def suggest_book():
	data = request.get_json()
	book = Book(data['title'], data['author'])
	books[data['title']] = book
	return 'Book suggested successfully', 201

@app.route('/vote_for_book', methods=['POST'])
def vote_for_book():
	data = request.get_json()
	book = books.get(data['title'])
	if book:
		book.votes += 1
		return 'Vote counted successfully', 200
	else:
		return 'Book not found', 404

@app.route('/select_next_book', methods=['GET'])
def select_next_book():
	most_votes = 0
	selected_book = None
	for book in books.values():
		if book.votes > most_votes:
			most_votes = book.votes
			selected_book = book
	if selected_book:
		return {'title': selected_book.title, 'author': selected_book.author}, 200
	else:
		return 'No books found', 404

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		user.interests = data.get('interests', user.interests)
		user.books_read = data.get('books_read', user.books_read)
		return 'Profile updated successfully', 200
	else:
		return 'User not found', 404

@app.route('/view_profile', methods=['GET'])
def view_profile():
	username = request.args.get('username')
	user = users.get(username)
	if user:
		return {'username': user.username, 'email': user.email, 'interests': user.interests, 'books_read': user.books_read, 'followed_users': [u.username for u in user.followed_users]}, 200
	else:
		return 'User not found', 404

@app.route('/follow_user', methods=['POST'])
def follow_user():
	data = request.get_json()
	user = users.get(data['username'])
	user_to_follow = users.get(data['user_to_follow'])
	if user and user_to_follow:
		user.followed_users.append(user_to_follow)
		return 'User followed successfully', 200
	else:
		return 'User not found', 404

@app.route('/recommend_books', methods=['GET'])
def recommend_books():
	username = request.args.get('username')
	user = users.get(username)
	if user:
		# Get the books read by the user
		books_read_by_user = set(user.books_read)
		# Get the top 5 books with the most votes
		top_books = sorted(books.values(), key=lambda book: book.votes, reverse=True)[:5]
		# Recommend the top books that the user hasn't read yet
		recommendations = [book for book in top_books if book.title not in books_read_by_user]
		return {'recommendations': [{'title': book.title, 'author': book.author} for book in recommendations]}, 200
	else:
		return 'User not found', 404

# Admin routes
@app.route('/admin/manage_bookclub', methods=['POST'])
def manage_bookclub():
	data = request.get_json()
	bookclub = bookclubs.get(data['name'])
	if bookclub:
		bookclub.description = data.get('description', bookclub.description)
		bookclub.is_private = data.get('is_private', bookclub.is_private)
		return 'BookClub updated successfully', 200
	else:
		return 'BookClub not found', 404

@app.route('/admin/remove_user', methods=['DELETE'])
def remove_user():
	username = request.args.get('username')
	if username in users:
		del users[username]
		return 'User removed successfully', 200
	else:
		return 'User not found', 404

@app.route('/admin/remove_bookclub', methods=['DELETE'])
def remove_bookclub():
	name = request.args.get('name')
	if name in bookclubs:
		del bookclubs[name]
		return 'BookClub removed successfully', 200
	else:
		return 'BookClub not found', 404

@app.route('/admin/view_analytics', methods=['GET'])
def view_analytics():
	return {
		'number_of_users': len(users),
		'number_of_bookclubs': len(bookclubs),
		'most_popular_books': sorted(books.values(), key=lambda book: book.votes, reverse=True)[:5]
	}, 200

@app.route('/notifications', methods=['GET'])
def view_notifications():
	username = request.args.get('username')
	user = users.get(username)
	if user:
		return {'notifications': [{'message': n.message, 'read': n.read} for n in user.notifications]}, 200
	else:
		return 'User not found', 404

@app.route('/notifications', methods=['POST'])
def mark_notifications_as_read():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		for n in user.notifications:
			n.read = True
		return 'Notifications marked as read', 200
	else:
		return 'User not found', 404

@app.route('/resources', methods=['POST'])
def add_resource():
	data = request.get_json()
	user = users.get(data['username'])
	if user:
		resource = Resource(data['title'], data['content'], user)
		resources[data['title']] = resource
		return 'Resource added successfully', 201
	else:
		return 'User not found', 404

@app.route('/resources', methods=['GET'])
def view_resources():
	return {'resources': [{'title': r.title, 'content': r.content, 'user': r.user.username} for r in resources.values()]}, 200

@app.route('/resources', methods=['PUT'])
def update_resource():
	data = request.get_json()
	resource = resources.get(data['title'])
	if resource and resource.user.username == data['username']:
		resource.content = data['content']
		return 'Resource updated successfully', 200
	else:
		return 'Resource not found or user not authorized', 404

if __name__ == '__main__':
	app.run(debug=True)
