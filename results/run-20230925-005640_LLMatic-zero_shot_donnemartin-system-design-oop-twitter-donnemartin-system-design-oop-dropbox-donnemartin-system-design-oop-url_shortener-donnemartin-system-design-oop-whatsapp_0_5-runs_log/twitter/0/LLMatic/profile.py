from flask import Flask, request
from database import users_db, user_schema

app = Flask(__name__)

@app.route('/profile', methods=['GET', 'PUT'])
def profile():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	if request.method == 'GET':
		return user, 200

	data = request.get_json()
	for field in user_schema:
		if field in data:
			user[field] = data[field]

	return user, 200
