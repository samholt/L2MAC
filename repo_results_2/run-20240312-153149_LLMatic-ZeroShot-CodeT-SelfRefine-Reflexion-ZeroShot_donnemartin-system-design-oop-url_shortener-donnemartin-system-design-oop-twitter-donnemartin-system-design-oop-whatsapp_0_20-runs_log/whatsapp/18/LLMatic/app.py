from flask import Flask, request, jsonify, render_template
from mock_db import MockDB
import base64
import datetime

app = Flask(__name__)
db = MockDB()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		data = request.form
		if 'email' not in data or 'password' not in data:
			return jsonify({'message': 'Missing email or password'}), 400
		db.add_user(data['email'], data['password'])
		return jsonify({'message': 'User registered successfully'}), 200
	else:
		return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		data = request.form
		if 'email' not in data or 'password' not in data:
			return jsonify({'message': 'Missing email or password'}), 400
		user = db.get_user(data['email'], data['password'])
		if user is None:
			return jsonify({'message': 'Invalid email or password'}), 400
		db.update_last_activity(data['email'])
		return jsonify({'message': 'User logged in successfully'}), 200
	else:
		return render_template('login.html')

@app.route('/profile/<email>', methods=['GET'])
def profile(email):
	user = db.get_user(email)
	if user is None:
		return jsonify({'message': 'User not found'}), 404
	last_activity = db.get_last_activity(email)
	status = 'Online' if last_activity and (datetime.datetime.now() - last_activity).total_seconds() < 300 else 'Offline'
	return render_template('profile.html', email=user['email'], status=status, picture=user['picture'])

@app.route('/group_chat/<group_name>', methods=['GET'])
def group_chat(group_name):
	group = db.get_group(group_name)
	if group is None:
		return jsonify({'message': 'Group not found'}), 404
	return render_template('group_chat.html', group_name=group['name'], messages=group['messages'])

@app.route('/status/<user_id>', methods=['GET'])
def status(user_id):
	status = db.get_status(user_id)
	if status is None:
		return jsonify({'message': 'Status not found'}), 404
	return render_template('status.html', image=status['image'], visibility=status['visibility'])

@app.route('/post-status', methods=['POST'])
def post_status():
	data = request.json
	if 'user_id' not in data or 'image' not in data:
		return jsonify({'message': 'Missing user_id or image'}), 400
	db.post_status(data['user_id'], data['image'])
	return jsonify({'message': 'Status posted successfully'}), 200

@app.route('/update-status-visibility', methods=['POST'])
def update_status_visibility():
	data = request.json
	if 'user_id' not in data or 'visibility' not in data:
		return jsonify({'message': 'Missing user_id or visibility'}), 400
	db.update_status_visibility(data['user_id'], data['visibility'])
	return jsonify({'message': 'Status visibility updated successfully'}), 200

@app.route('/create-group', methods=['POST'])
def create_group():
	data = request.json
	if 'email' not in data or 'group_name' not in data or 'members' not in data:
		return jsonify({'message': 'Missing email, group_name or members'}), 400
	db.create_group(data['email'], data['group_name'], data['members'])
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/edit-group', methods=['POST'])
def edit_group():
	data = request.json
	if 'email' not in data or 'group_name' not in data or 'members' not in data:
		return jsonify({'message': 'Missing email, group_name or members'}), 400
	db.edit_group(data['email'], data['group_name'], data['members'])
	return jsonify({'message': 'Group edited successfully'}), 200

@app.route('/add-group-admin', methods=['POST'])
def add_group_admin():
	data = request.json
	if 'email' not in data or 'group_name' not in data or 'admin_email' not in data:
		return jsonify({'message': 'Missing email, group_name or admin_email'}), 400
	db.add_group_admin(data['email'], data['group_name'], data['admin_email'])
	return jsonify({'message': 'Admin added successfully'}), 200

@app.route('/remove-group-admin', methods=['POST'])
def remove_group_admin():
	data = request.json
	if 'email' not in data or 'group_name' not in data or 'admin_email' not in data:
		return jsonify({'message': 'Missing email, group_name or admin_email'}), 400
	db.remove_group_admin(data['email'], data['group_name'], data['admin_email'])
	return jsonify({'message': 'Admin removed successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
