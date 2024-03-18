from flask import Flask, request, jsonify
from dataclasses import dataclass
import jwt

app = Flask(__name__)

users = {}
posts = {}

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str
	website: str
	location: str
	is_private: bool
	followers: list
	following: list

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str
	likes: int
	retweets: int
	replies: list

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	id = len(users)
	user = User(id, data['username'], data['email'], data['password'], '', '', '', False, [], [])
	users[id] = user
	return jsonify({'id': id}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for id, user in users.items():
		if user.username == data['username'] and user.password == data['password']:
			token = jwt.encode({'id': id}, 'secret', algorithm='HS256')
			return jsonify({'token': token}), 200
	return 'Invalid username or password', 401

@app.route('/users/<int:id>', methods=['GET', 'PUT'])
def user(id):
	if id not in users:
		return 'User not found', 404
	if request.method == 'GET':
		user = users[id]
		return jsonify({'username': user.username, 'email': user.email, 'bio': user.bio, 'website': user.website, 'location': user.location, 'is_private': user.is_private, 'followers': user.followers, 'following': user.following}), 200
	elif request.method == 'PUT':
		data = request.get_json()
		user = users[id]
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		user.is_private = data.get('is_private', user.is_private)
		return 'Profile updated', 200

@app.route('/posts', methods=['POST'])
def create_post():
	data = request.get_json()
	id = len(posts)
	post = Post(id, data['user_id'], data['content'], data.get('image', ''), 0, 0, [])
	posts[id] = post
	return jsonify({'id': id}), 201

@app.route('/posts/<int:id>', methods=['GET', 'DELETE'])
def post(id):
	if id not in posts:
		return 'Post not found', 404
	if request.method == 'GET':
		post = posts[id]
		return jsonify({'user_id': post.user_id, 'content': post.content, 'image': post.image, 'likes': post.likes, 'retweets': post.retweets, 'replies': post.replies}), 200
	elif request.method == 'DELETE':
		del posts[id]
		return 'Post deleted', 200

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	follower = users[data['follower_id']]
	followee = users[data['followee_id']]
	if followee.is_private:
		return 'Cannot follow private user', 403
	follower.following.append(followee.id)
	followee.followers.append(follower.id)
	return 'Followed user', 200

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	follower = users[data['follower_id']]
	followee = users[data['followee_id']]
	follower.following.remove(followee.id)
	followee.followers.remove(follower.id)
	return 'Unfollowed user', 200

@app.route('/timeline/<int:id>', methods=['GET'])
def timeline(id):
	user = users[id]
	timeline_posts = [post for post in posts.values() if post.user_id in user.following]
	return jsonify([{'user_id': post.user_id, 'content': post.content, 'image': post.image, 'likes': post.likes, 'retweets': post.retweets, 'replies': post.replies} for post in timeline_posts]), 200

if __name__ == '__main__':
	app.run(debug=True)
