from flask import Flask, request
from database import users_db, posts_db, interactions_db, interaction_schema

app = Flask(__name__)

@app.route('/interact', methods=['POST'])
def interact():
	user_email = request.headers.get('Authorization')
	user = users_db.get(user_email)

	if not user:
		return {'message': 'User not found.'}, 404

	data = request.get_json()
	for field in interaction_schema:
		if field not in data:
			return {'message': f'Missing field: {field}'}, 400

	data['user_email'] = user_email
	interactions_db[data['interaction_id']] = data

	return {'message': 'Interaction created.'}, 201
