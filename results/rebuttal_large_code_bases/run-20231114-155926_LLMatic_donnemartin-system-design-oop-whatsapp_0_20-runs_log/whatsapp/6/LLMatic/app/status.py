from flask import Blueprint, request, jsonify
from .models import User, Status
from datetime import datetime

status = Blueprint('status', __name__)

users = []
statuses = []

@status.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user = [u for u in users if u.username == data['username']]
	if not user:
		return jsonify({'message': 'User not found!'}), 404
	new_status = Status(id=len(statuses)+1, user=user[0], image='', timestamp=datetime.now(), visibility='')
	user[0].status_message = data['content']
	statuses.append(new_status)
	return jsonify({'message': 'Status posted successfully!'}), 200

@status.route('/view_status/<username>', methods=['GET'])
def view_status(username):
	user = [u for u in users if u.username == username]
	if not user:
		return jsonify({'message': 'User not found!'}), 404
	status = [s for s in statuses if s.user == user[0]]
	return jsonify({'status': [s.user.status_message for s in status]}), 200
