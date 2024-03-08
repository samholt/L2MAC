from flask import Flask, request
import auth
import post
import message
import notification

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = auth.register_user(data['email'], data['username'], data['password'])
	return {'message': 'User registered successfully', 'user': user.__dict__}, 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	token = auth.authenticate_user(data['username'], data['password'])
	if token:
		return {'message': 'Login successful', 'token': token}, 200
	else:
		return {'message': 'Invalid credentials'}, 401

@app.route('/update_profile', methods=['POST'])
def update_profile():
	data = request.get_json()
	user = auth.update_profile(data['username'], data.get('profile_picture'), data.get('bio'), data.get('website_link'), data.get('location'), data.get('visibility'))
	if user:
		return {'message': 'Profile updated successfully', 'user': user.__dict__}, 200
	else:
		return {'message': 'User not found'}, 404

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	result = auth.follow_user(data['username'], data['user_to_follow'])
	if result:
		return {'message': 'Followed user successfully'}, 200
	else:
		return {'message': 'Failed to follow user'}, 400

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	result = auth.unfollow_user(data['username'], data['user_to_unfollow'])
	if result:
		return {'message': 'Unfollowed user successfully'}, 200
	else:
		return {'message': 'Failed to unfollow user'}, 400

@app.route('/create_post', methods=['POST'])
def create_post():
	data = request.get_json()
	new_post = post.create_post(data['user'], data.get('text'), data.get('images'))
	return {'message': 'Post created successfully', 'post': new_post.__dict__}, 201

@app.route('/delete_post', methods=['DELETE'])
def delete_post():
	data = request.get_json()
	result = post.delete_post(int(data['post_id']))
	if result:
		return {'message': 'Post deleted successfully'}, 200
	else:
		return {'message': 'Post not found'}, 404

@app.route('/search', methods=['GET'])
def search():
	keyword = request.args.get('keyword')
	results = post.search(keyword)
	return {'message': 'Search results', 'results': results}, 200

@app.route('/filter', methods=['GET'])
def filter():
	content = request.args.get('content')
	results = post.filter(content)
	return {'message': 'Filter results', 'results': results}, 200

@app.route('/trending', methods=['GET'])
def trending():
	results = post.get_trending_topics()
	return {'message': 'Trending topics', 'results': results}, 200

@app.route('/recommendations', methods=['GET'])
def recommendations():
	username = request.args.get('username')
	results = post.get_user_recommendations(username)
	return {'message': 'User recommendations', 'results': results}, 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	new_message = message.send_message(data['text'], data['sender'], data['receiver'])
	if new_message:
		return {'message': 'Message sent successfully', 'message': new_message.__dict__}, 201
	else:
		return {'message': 'Failed to send message'}, 400

@app.route('/block_user', methods=['POST'])
def block_user():
	data = request.get_json()
	result = message.block_user(data['username'], data['user_to_block'])
	if result:
		return {'message': 'Blocked user successfully'}, 200
	else:
		return {'message': 'Failed to block user'}, 400

@app.route('/unblock_user', methods=['POST'])
def unblock_user():
	data = request.get_json()
	result = message.unblock_user(data['username'], data['user_to_unblock'])
	if result:
		return {'message': 'Unblocked user successfully'}, 200
	else:
		return {'message': 'Failed to unblock user'}, 400

@app.route('/create_notification', methods=['POST'])
def create_notification():
	data = request.get_json()
	new_notification = notification.create_notification(data['user'], data['text'])
	return {'message': 'Notification created successfully', 'notification': new_notification.__dict__}, 201

if __name__ == '__main__':
	app.run(debug=True)
