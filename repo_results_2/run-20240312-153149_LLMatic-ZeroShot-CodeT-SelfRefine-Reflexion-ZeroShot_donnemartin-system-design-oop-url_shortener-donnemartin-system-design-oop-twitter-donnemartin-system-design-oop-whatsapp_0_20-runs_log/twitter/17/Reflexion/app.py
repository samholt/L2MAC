from flask import Flask, request, jsonify
from models import User, Post, Comment, Message, Notification
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)

# Mock database
users = {}
posts = {}
comments = {}
messages = {}
notifications = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	username = data.get('username')
	email = data.get('email')
	password = data.get('password')
	if username in users:
		return jsonify({'message': 'User already exists'}), 400
	users[username] = User(username, email, password)
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')
	user = users.get(username)
	if not user or not user.check_password(password):
		return jsonify({'message': 'Invalid username or password'}), 400
	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200

@app.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
	username = get_jwt_identity()
	user = users.get(username)
	if request.method == 'GET':
		return jsonify(user.to_dict()), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user.update_profile(data)
		return jsonify({'message': 'Profile updated successfully'}), 200

@app.route('/post', methods=['POST', 'DELETE'])
@jwt_required()
def post():
	username = get_jwt_identity()
	user = users.get(username)
	if request.method == 'POST':
		data = request.get_json()
		content = data.get('content')
		image_url = data.get('image_url')
		post = Post(username, content, image_url)
		posts[post.id] = post
		return jsonify({'message': 'Post created successfully'}), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		post_id = data.get('post_id')
		post = posts.get(post_id)
		if not post or post.username != username:
			return jsonify({'message': 'Post not found'}), 404
		del posts[post_id]
		return jsonify({'message': 'Post deleted successfully'}), 200

@app.route('/comment', methods=['POST', 'DELETE'])
@jwt_required()
def comment():
	username = get_jwt_identity()
	user = users.get(username)
	if request.method == 'POST':
		data = request.get_json()
		post_id = data.get('post_id')
		content = data.get('content')
		comment = Comment(username, post_id, content)
		comments[comment.id] = comment
		return jsonify({'message': 'Comment created successfully'}), 200
	elif request.method == 'DELETE':
		data = request.get_json()
		comment_id = data.get('comment_id')
		comment = comments.get(comment_id)
		if not comment or comment.username != username:
			return jsonify({'message': 'Comment not found'}), 404
		del comments[comment_id]
		return jsonify({'message': 'Comment deleted successfully'}), 200

@app.route('/message', methods=['POST'])
@jwt_required()
def message():
	username = get_jwt_identity()
	user = users.get(username)
	data = request.get_json()
	recipient_username = data.get('recipient_username')
	content = data.get('content')
	message = Message(username, recipient_username, content)
	messages[message.id] = message
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/notification', methods=['GET'])
@jwt_required()
def notification():
	username = get_jwt_identity()
	user = users.get(username)
	notifications = [n.to_dict() for n in notifications.values() if n.recipient_username == username]
	return jsonify(notifications), 200

if __name__ == '__main__':
	app.run(debug=True)
