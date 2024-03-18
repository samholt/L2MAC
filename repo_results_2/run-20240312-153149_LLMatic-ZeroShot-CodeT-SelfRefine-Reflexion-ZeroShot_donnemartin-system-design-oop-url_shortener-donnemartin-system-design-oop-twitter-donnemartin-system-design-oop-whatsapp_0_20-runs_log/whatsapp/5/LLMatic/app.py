from flask import Flask, request, jsonify
from user import User
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	user = User(data['email'], data['password'], '', '', '')
	return jsonify({'message': user.signup(data['email'], data['password'])})

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'password': user.recover_password(data['email'])})

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.set_profile_picture(data['picture'])})

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.set_status_message(data['message'])})

@app.route('/manage_privacy_settings', methods=['POST'])
def manage_privacy_settings():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.manage_privacy_settings(data['settings'])})

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.block_contact(data['contact'])})

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.unblock_contact(data['contact'])})

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.create_group(data['group_name'])})

@app.route('/add_contact_to_group', methods=['POST'])
def add_contact_to_group():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.add_contact_to_group(data['group_name'], data['contact'])})

@app.route('/remove_contact_from_group', methods=['POST'])
def remove_contact_from_group():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.remove_contact_from_group(data['group_name'], data['contact'])})

@app.route('/delete_group', methods=['POST'])
def delete_group():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.delete_group(data['group_name'])})

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	return jsonify({'message': user.post_status(data['message'], data['visibility'])})

@app.route('/view_statuses', methods=['GET'])
def view_statuses():
	data = request.get_json()
	user = User(data['email'], '', '', '', '')
	statuses = user.view_statuses()
	return jsonify({'statuses': [status.message for status in statuses]})

if __name__ == '__main__':
	app.run(debug=True)
