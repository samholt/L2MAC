from flask import Flask, request
from database import users_db, posts_db, follows_db, notifications_db, user_schema, post_schema, follow_schema, notification_schema

app = Flask(__name__)

@app.route('/follow', methods=['POST'])
def follow():
	data = request.get_json()
	for field in follow_schema:
		if field not in data:
			return {'message': f'Missing field: {field}'}, 400

	follows_db[data['follower_id']] = data

	# Notify the user being followed
	notification = {
		'user_id': data['followee_id'],
		'content': f"{data['follower_id']} has started following you.",
		'timestamp': data['timestamp']
	}

	notifications_db[data['followee_id']] = notification

	return {'message': 'Followed user.'}, 201

@app.route('/unfollow', methods=['POST'])
def unfollow():
	data = request.get_json()
	follower_id = data.get('follower_id')
	followee_id = data.get('followee_id')

	if follower_id in follows_db and follows_db[follower_id]['followee_id'] == followee_id:
		del follows_db[follower_id]
		return {'message': 'Unfollowed user.'}, 200

	return {'message': 'You are not following this user.'}, 400

@app.route('/timeline', methods=['GET'])
def timeline():
	user_id = request.args.get('user_id')
	if user_id not in users_db:
		return {'message': 'User not found.'}, 404

	# Get all users that the current user is following
	following = [follow['followee_id'] for follow in follows_db.values() if follow['follower_id'] == user_id]

	# Get all posts from users that the current user is following
	timeline_posts = [post for post in posts_db.values() if post['user_id'] in following]

	return {'timeline': timeline_posts}, 200
