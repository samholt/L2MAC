from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from dataclasses import dataclass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

mock_db = {}
post_id = 0

@dataclass
class User:
	email: str
	username: str
	password: str
	profile: 'Profile'
	posts: list
	followers: list
	following: list
	messages: list

@dataclass
class Profile:
	bio: str
	website: str
	location: str
	is_private: bool

@dataclass
class Post:
	id: int
	user: 'User'
	content: str
	images: list
	likes: int
	retweets: int
	replies: list

@dataclass
class Message:
	from_user: 'User'
	to_user: 'User'
	content: str

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if not username or not email or not password:
		return jsonify({'message': 'Invalid input'}), 400
	hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
	new_user = User(email, username, hashed_password, Profile('', '', '', False), [], [], [])
	mock_db[username] = new_user
	return jsonify({'message': 'Registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = mock_db.get(username)
	if not user or not check_password_hash(user.password, password):
		return jsonify({'message': 'Invalid username or password'}), 401
	token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token}), 200

@app.route('/profile/<username>', methods=['GET', 'PUT'])
def profile(username):
	user = mock_db.get(username)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	if request.method == 'GET':
		if user.profile.is_private:
			return jsonify({'message': 'Profile is private'}), 403
		return jsonify(user.profile), 200
	elif request.method == 'PUT':
		data = request.get_json()
		bio = data.get('bio')
		website = data.get('website')
		location = data.get('location')
		is_private = data.get('is_private')
		user.profile.bio = bio if bio else user.profile.bio
		user.profile.website = website if website else user.profile.website
		user.profile.location = location if location else user.profile.location
		user.profile.is_private = is_private if is_private is not None else user.profile.is_private
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	username = data.get('username')
	to_follow = data.get('to_follow')
	user = mock_db.get(username)
	follow_user = mock_db.get(to_follow)
	if not user or not follow_user:
		return jsonify({'message': 'User not found'}), 404
	if follow_user in user.following:
		return jsonify({'message': 'Already following'}), 400
	user.following.append(follow_user)
	follow_user.followers.append(user)
	return jsonify({'message': 'Followed successfully'}), 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	username = data.get('username')
	to_unfollow = data.get('to_unfollow')
	user = mock_db.get(username)
	unfollow_user = mock_db.get(to_unfollow)
	if not user or not unfollow_user:
		return jsonify({'message': 'User not found'}), 404
	if unfollow_user not in user.following:
		return jsonify({'message': 'Not following'}), 400
	user.following.remove(unfollow_user)
	unfollow_user.followers.remove(user)
	return jsonify({'message': 'Unfollowed successfully'}), 200

@app.route('/feed/<username>', methods=['GET'])
def feed(username):
	user = mock_db.get(username)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	feed = []
	for following in user.following:
		for post in following.posts:
			feed.append({'username': following.username, 'post_id': post.id, 'content': post.content})
	return jsonify(feed), 200

@app.route('/message', methods=['POST'])
def message():
	data = request.get_json()
	from_username = data.get('from_username')
	to_username = data.get('to_username')
	content = data.get('content')
	from_user = mock_db.get(from_username)
	to_user = mock_db.get(to_username)
	if not from_user or not to_user or not content:
		return jsonify({'message': 'Invalid input'}), 400
	message = Message(from_user, to_user, content)
	from_user.messages.append(message)
	to_user.messages.append(message)
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/messages/<username>', methods=['GET'])
def messages(username):
	user = mock_db.get(username)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	messages = []
	for message in user.messages:
		messages.append({'from': message.from_user.username, 'to': message.to_user.username, 'content': message.content})
	return jsonify(messages), 200

@app.route('/post', methods=['POST'])
def post():
	global post_id
	data = request.get_json()
	username = data.get('username')
	content = data.get('content')
	images = data.get('images')
	user = mock_db.get(username)
	if not user or not content:
		return jsonify({'message': 'Invalid input'}), 400
	post_id += 1
	new_post = Post(post_id, user, content, images, 0, 0, [])
	user.posts.append(new_post)
	return jsonify({'message': 'Post created successfully'}), 200

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	for user in mock_db.values():
		for post in user.posts:
			if post.id == post_id:
				user.posts.remove(post)
				return jsonify({'message': 'Post deleted successfully'}), 200
	return jsonify({'message': 'Post not found'}), 404

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	if not keyword:
		return jsonify({'message': 'Invalid input'}), 400
	results = []
	for user in mock_db.values():
		if keyword in user.username:
			results.append({'type': 'user', 'username': user.username})
		for post in user.posts:
			if keyword in post.content:
				results.append({'type': 'post', 'post_id': post.id, 'content': post.content})
	return jsonify(results), 200

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
