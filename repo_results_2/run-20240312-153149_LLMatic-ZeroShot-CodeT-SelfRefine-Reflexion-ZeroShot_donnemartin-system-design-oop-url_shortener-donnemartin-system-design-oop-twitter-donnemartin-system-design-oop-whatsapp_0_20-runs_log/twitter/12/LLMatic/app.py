from flask import Flask, request, jsonify
from dataclasses import dataclass, field
import jwt
import datetime
from collections import Counter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

users_db = {}
posts_db = {}
messages_db = {}
notifications_db = {}

@dataclass
class Profile:
	profile_picture: str
	bio: str
	website_link: str
	location: str

@dataclass
class User:
	email: str
	username: str
	password: str
	profile: Profile
	followers: list = field(default_factory=list)
	following: list = field(default_factory=list)

@dataclass
class Post:
	user: str
	content: str
	image: str
	likes: int = 0
	retweets: int = 0
	replies: list = field(default_factory=list)

@dataclass
class Message:
	sender: str
	recipient: str
	content: str

@dataclass
class Notification:
	user: str
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(email=data['email'], username=data['username'], password=data['password'], profile=Profile('', '', '', ''))
	users_db[new_user.email] = new_user
	return jsonify({'message': 'registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = users_db.get(data['email'])
	if not user or user.password != data['password']:
		return jsonify({'message': 'Bad Request'}), 400
	token = jwt.encode({'user': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	user = users_db.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 400
	user.profile = Profile(data['profile_picture'], data['bio'], data['website_link'], data['location'])
	return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	user = users_db.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 400
	new_post = Post(user=user.email, content=data['content'], image=data.get('image', ''))
	posts_db[len(posts_db)] = new_post
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/like_post', methods=['POST'])
def like_post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	post = posts_db.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 400
	post.likes += 1
	return jsonify({'message': 'Post liked successfully'}), 200

@app.route('/retweet_post', methods=['POST'])
def retweet_post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	post = posts_db.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 400
	post.retweets += 1
	return jsonify({'message': 'Post retweeted successfully'}), 200

@app.route('/reply_post', methods=['POST'])
def reply_post():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	post = posts_db.get(data['post_id'])
	if not post:
		return jsonify({'message': 'Post not found'}), 400
	post.replies.append(data['reply'])
	return jsonify({'message': 'Reply added successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	user = users_db.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 400
	user_to_follow = users_db.get(data['user_to_follow'])
	if not user_to_follow:
		return jsonify({'message': 'User to follow not found'}), 400
	user.following.append(user_to_follow.email)
	user_to_follow.followers.append(user.email)
	return jsonify({'message': 'Followed successfully'}), 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	user = users_db.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 400
	user_to_unfollow = users_db.get(data['user_to_unfollow'])
	if not user_to_unfollow:
		return jsonify({'message': 'User to unfollow not found'}), 400
	if user_to_unfollow.email in user.following:
		user.following.remove(user_to_unfollow.email)
	if user.email in user_to_unfollow.followers:
		user_to_unfollow.followers.remove(user.email)
	return jsonify({'message': 'Unfollowed successfully'}), 200

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	results = [post for post in posts_db.values() if query in post.content]
	return jsonify({'results': [post.__dict__ for post in results]}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	sender = users_db.get(decoded['user'])
	if not sender:
		return jsonify({'message': 'Sender not found'}), 400
	recipient = users_db.get(data['recipient'])
	if not recipient:
		return jsonify({'message': 'Recipient not found'}), 400
	new_message = Message(sender=sender.email, recipient=recipient.email, content=data['content'])
	messages_db[len(messages_db)] = new_message
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	token = data.get('token')
	if not token:
		return jsonify({'message': 'Token is missing'}), 400
	try:
		decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
	except:
		return jsonify({'message': 'Token is invalid'}), 400
	user = users_db.get(decoded['user'])
	if not user:
		return jsonify({'message': 'User not found'}), 400
	new_notification = Notification(user=user.email, content=data['content'])
	notifications_db[len(notifications_db)] = new_notification
	return jsonify({'message': 'Notification created successfully'}), 200

@app.route('/trending', methods=['GET'])
def trending():
	words = [word for post in posts_db.values() for word in post.content.split()]
	counter = Counter(words)
	trending = counter.most_common(10)
	return jsonify({'trending': trending}), 200

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
