from flask import Flask, request, jsonify
from user import User
from post import Post
from trending import Trending

app = Flask(__name__)

# Mock databases
users = {}
posts = {}
trending = Trending()

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	email = data.get('email')
	username = data.get('username')
	password = data.get('password')
	if email in users:
		return jsonify({'message': 'Email already exists.'}), 400
	if username in users:
		return jsonify({'message': 'Username already exists.'}), 400
	user = User(email, username, password)
	users[username] = user
	return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid username or password.'}), 401
	token = user.generate_jwt()
	return jsonify({'token': token}), 200

@app.route('/post', methods=['POST'])
def create_post():
	data = request.get_json()
	username = data.get('username')
	text = data.get('text')
	user = users.get(username)
	if not user:
		return jsonify({'message': 'User not found.'}), 404
	post = Post(text)
	posts[len(posts)] = post
	return jsonify({'message': 'Post created successfully.'}), 201

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found.'}), 404
	post.delete()
	return jsonify({'message': 'Post deleted successfully.'}), 200

@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found.'}), 404
	post.like()
	return jsonify({'message': 'Post liked successfully.'}), 200

@app.route('/post/<int:post_id>/retweet', methods=['POST'])
def retweet_post(post_id):
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found.'}), 404
	post.retweet()
	return jsonify({'message': 'Post retweeted successfully.'}), 200

@app.route('/post/<int:post_id>/reply', methods=['POST'])
def reply_post(post_id):
	data = request.get_json()
	reply = data.get('reply')
	post = posts.get(post_id)
	if not post:
		return jsonify({'message': 'Post not found.'}), 404
	post.reply(reply)
	return jsonify({'message': 'Reply posted successfully.'}), 200

@app.route('/user/<string:username>/follow', methods=['POST'])
def follow_user(username):
	data = request.get_json()
	follower_username = data.get('follower_username')
	user = users.get(username)
	follower = users.get(follower_username)
	if not user or not follower:
		return jsonify({'message': 'User not found.'}), 404
	follower.follow(user)
	return jsonify({'message': 'User followed successfully.'}), 200

@app.route('/user/<string:username>/unfollow', methods=['POST'])
def unfollow_user(username):
	data = request.get_json()
	follower_username = data.get('follower_username')
	user = users.get(username)
	follower = users.get(follower_username)
	if not user or not follower:
		return jsonify({'message': 'User not found.'}), 404
	follower.unfollow(user)
	return jsonify({'message': 'User unfollowed successfully.'}), 200

@app.route('/user/<string:username>/block', methods=['POST'])
def block_user(username):
	data = request.get_json()
	blocker_username = data.get('blocker_username')
	user = users.get(username)
	blocker = users.get(blocker_username)
	if not user or not blocker:
		return jsonify({'message': 'User not found.'}), 404
	blocker.block(user)
	return jsonify({'message': 'User blocked successfully.'}), 200

@app.route('/user/<string:username>/unblock', methods=['POST'])
def unblock_user(username):
	data = request.get_json()
	blocker_username = data.get('blocker_username')
	user = users.get(username)
	blocker = users.get(blocker_username)
	if not user or not blocker:
		return jsonify({'message': 'User not found.'}), 404
	blocker.unblock(user)
	return jsonify({'message': 'User unblocked successfully.'}), 200

@app.route('/user/<string:username>/notifications', methods=['GET'])
def get_notifications(username):
	user = users.get(username)
	if not user:
		return jsonify({'message': 'User not found.'}), 404
	return jsonify({'notifications': user.notifications}), 200

@app.route('/trending/hashtags', methods=['GET'])
def get_trending_hashtags():
	trending.identify_trending_hashtags(posts.values())
	return jsonify({'trending_hashtags': trending.display_trending_hashtags()}), 200

@app.route('/trending/topics', methods=['GET'])
def get_trending_topics():
	trending.identify_trending_topics(posts.values())
	return jsonify({'trending_topics': trending.display_trending_topics()}), 200

@app.route('/user/<string:username>/recommendations', methods=['GET'])
def get_user_recommendations(username):
	user = users.get(username)
	if not user:
		return jsonify({'message': 'User not found.'}), 404
	return jsonify({'recommendations': trending.recommend_users(user, users.values())}), 200

if __name__ == '__main__':
	app.run(debug=True)
