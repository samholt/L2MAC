from flask import Flask, request
from database import trends_db, trend_schema, users_db, follows_db

app = Flask(__name__)

@app.route('/trending', methods=['GET'])
def trending():
	# Get all trends
	trends = list(trends_db.values())

	# Sort trends by mentions
	trends.sort(key=lambda x: x['mentions'], reverse=True)

	return {'trends': trends}, 200

@app.route('/recommendations', methods=['GET'])
def recommendations(user_id):
	if user_id not in users_db:
		return {'message': 'User not found.'}, 404

	# Get all users that the current user is not following
	not_following = [user for user in users_db.values() if user['user_id'] != user_id and user['user_id'] not in follows_db]

	# Recommend users based on mutual followers
	recommendations = sorted(not_following, key=lambda x: len([follow for follow in follows_db.values() if follow['followee_id'] == x['user_id']]), reverse=True)

	return {'recommendations': recommendations}, 200
