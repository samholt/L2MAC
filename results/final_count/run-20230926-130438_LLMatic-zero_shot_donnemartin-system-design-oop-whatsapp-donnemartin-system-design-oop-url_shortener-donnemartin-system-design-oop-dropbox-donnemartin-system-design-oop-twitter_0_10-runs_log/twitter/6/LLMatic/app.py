from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from dataclasses import dataclass, field

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

@dataclass
class User:
	email: str
	username: str
	password: str
	following: list = field(default_factory=list)
	followers: list = field(default_factory=list)
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None

@dataclass
class Post:
	id: int
	username: str
	text: str
	images: list = field(default_factory=list)
	likes: int = 0
	retweets: int = 0
	comments: list = field(default_factory=list)

@dataclass
class Comment:
	username: str
	text: str

@dataclass
class Message:
	sender: str
	recipient: str
	text: str

@dataclass
class Notification:
	username: str
	text: str

users_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}
post_id = 0

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = generate_password_hash(data.get('password'))
	user = User(email, username, password)
	users_db[username] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users_db.get(username)
	if user and check_password_hash(user.password, password):
		token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
		return jsonify({'token': token}), 200
	return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	token = data.get('token')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		user = users_db.get(username)
		if user:
			user.profile_picture = data.get('profile_picture', user.profile_picture)
			user.bio = data.get('bio', user.bio)
			user.website_link = data.get('website_link', user.website_link)
			user.location = data.get('location', user.location)
			return jsonify({'message': 'Profile updated successfully'}), 200
		else:
			return jsonify({'message': 'User not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	token = data.get('token')
	follow_username = data.get('follow_username')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		user = users_db.get(username)
		follow_user = users_db.get(follow_username)
		if user and follow_user and follow_username not in user.following:
			user.following.append(follow_username)
			follow_user.followers.append(username)
			return jsonify({'message': 'User followed successfully'}), 200
		else:
			return jsonify({'message': 'User not found or already followed'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	token = data.get('token')
	unfollow_username = data.get('unfollow_username')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		user = users_db.get(username)
		unfollow_user = users_db.get(unfollow_username)
		if user and unfollow_user and unfollow_username in user.following:
			user.following.remove(unfollow_username)
			unfollow_user.followers.remove(username)
			return jsonify({'message': 'User unfollowed successfully'}), 200
		else:
			return jsonify({'message': 'User not found or not followed'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/timeline', methods=['POST'])
def timeline():
	data = request.get_json()
	token = data.get('token')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		user = users_db.get(username)
		if user:
			timeline_posts = [post for post_id, post in posts_db.items() if post.username in user.following]
			return jsonify({'timeline_posts': [post.__dict__ for post in timeline_posts]}), 200
		else:
			return jsonify({'message': 'User not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/create_post', methods=['POST'])
def create_post():
	global post_id
	data = request.get_json()
	token = data.get('token')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		user = users_db.get(username)
		if user:
			text = data.get('text')
			images = data.get('images', [])
			post = Post(post_id, username, text, images)
			posts_db[post_id] = post
			post_id += 1
			return jsonify({'message': 'Post created successfully', 'post_id': post_id-1}), 201
		else:
			return jsonify({'message': 'User not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	token = data.get('token')
	post_id = data.get('post_id')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		post = posts_db.get(post_id)
		if post and post.username == username:
			del posts_db[post_id]
			return jsonify({'message': 'Post deleted successfully'}), 200
		else:
			return jsonify({'message': 'Post not found or unauthorized'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/like_post', methods=['POST'])
def like_post():
	data = request.get_json()
	token = data.get('token')
	post_id = int(data.get('post_id'))
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		post = posts_db.get(post_id)
		if post:
			post.likes += 1
			return jsonify({'message': 'Post liked successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/retweet_post', methods=['POST'])
def retweet_post():
	data = request.get_json()
	token = data.get('token')
	post_id = int(data.get('post_id'))
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		post = posts_db.get(post_id)
		if post:
			post.retweets += 1
			return jsonify({'message': 'Post retweeted successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/reply_post', methods=['POST'])
def reply_post():
	data = request.get_json()
	token = data.get('token')
	post_id = int(data.get('post_id'))
	comment_text = data.get('comment_text')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		post = posts_db.get(post_id)
		if post:
			comment = Comment(username, comment_text)
			post.comments.append(comment)
			return jsonify({'message': 'Comment added successfully'}), 200
		else:
			return jsonify({'message': 'Post not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/search', methods=['POST'])
def search():
	data = request.get_json()
	query = data.get('query')
	results = {'users': [], 'posts': []}
	for username, user in users_db.items():
		if query in username or query in user.bio:
			results['users'].append(username)
	for post_id, post in posts_db.items():
		if query in post.text:
			results['posts'].append(post_id)
	return jsonify(results), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	token = data.get('token')
	recipient = data.get('recipient')
	text = data.get('text')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		sender = decoded.get('username')
		if users_db.get(recipient):
			message = Message(sender, recipient, text)
			messages_db[(sender, recipient)].append(message)
			return jsonify({'message': 'Message sent successfully'}), 200
		else:
			return jsonify({'message': 'Recipient not found'}), 404
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/get_messages', methods=['POST'])
def get_messages():
	data = request.get_json()
	token = data.get('token')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		messages = [message.__dict__ for (sender, recipient), messages in messages_db.items() if recipient == username]
		return jsonify({'messages': messages}), 200
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/get_notifications', methods=['POST'])
def get_notifications():
	data = request.get_json()
	token = data.get('token')
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
		username = decoded.get('username')
		notifications = [notification.__dict__ for notification in notifications_db.get(username, [])]
		return jsonify({'notifications': notifications}), 200
	except:
		return jsonify({'message': 'Invalid token'}), 401

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
