from flask import Flask, request
from database import users_db, posts_db

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	data = request.get_json()
	search_term = data.get('search_term')
	search_results = {'users': [], 'posts': []}

	for email, user in users_db.items():
		if search_term in user['username'] or search_term in user['email']:
			search_results['users'].append(user)

	for post_id, post in posts_db.items():
		if search_term in post['content']:
			search_results['posts'].append(post)

	return search_results, 200
