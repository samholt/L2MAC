from flask import Flask, request
from database import users_db, posts_db, post_schema

app = Flask(__name__)

@app.route('/post', methods=['POST', 'DELETE'])
def post():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	if request.method == 'POST':
		data = request.get_json()
		for field in post_schema:
			if field not in data:
				return {'message': f'Missing field: {field}'}, 400

		if len(data['content']) > 280:
			return {'message': 'Post content exceeds 280 characters.'}, 400

		data['user_email'] = user_email
		posts_db[data['post_id']] = data

		return {'message': 'Post created.'}, 201

	elif request.method == 'DELETE':
		data = request.get_json()
		post_id = data.get('post_id')

		if post_id in posts_db and posts_db[post_id]['user_email'] == user_email:
			del posts_db[post_id]
			return {'message': 'Post deleted.'}, 200

		return {'message': 'Post not found or not owned by user.'}, 404
