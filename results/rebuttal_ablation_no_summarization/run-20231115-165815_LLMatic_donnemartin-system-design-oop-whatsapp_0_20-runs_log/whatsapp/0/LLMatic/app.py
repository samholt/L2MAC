from flask import Flask, request, jsonify
from user import User
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

user = User()
group = Group()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	response = user.register(data['email'], data['password'])
	return jsonify({'message': response}), 200

@app.route('/recover_password', methods=['POST'])
def recover_password():
	data = request.get_json()
	response = user.recover_password(data['email'], data['recovery'])
	return jsonify({'message': response}), 200

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	response = user.set_profile_picture(data['email'], data['picture'])
	return jsonify({'message': response}), 200

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	response = user.set_status_message(data['email'], data['message'])
	return jsonify({'message': response}), 200

@app.route('/update_privacy_settings', methods=['POST'])
def update_privacy_settings():
	data = request.get_json()
	response = user.update_privacy_settings(data['email'], data['details'], data['last_seen'])
	return jsonify({'message': response}), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	response = user.block_contact(data['email'], data['contact'])
	return jsonify({'message': response}), 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	response = user.unblock_contact(data['email'], data['contact'])
	return jsonify({'message': response}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	response = group.create_group(data['group_name'], data['admin'], data['picture'])
	return jsonify({'message': response}), 200

@app.route('/add_member', methods=['POST'])
def add_member():
	data = request.get_json()
	response = group.add_member(data['group_name'], data['member'])
	return jsonify({'message': response}), 200

@app.route('/remove_member', methods=['POST'])
def remove_member():
	data = request.get_json()
	response = group.remove_member(data['group_name'], data['member'])
	return jsonify({'message': response}), 200

@app.route('/block_member', methods=['POST'])
def block_member():
	data = request.get_json()
	response = group.block_member(data['group_name'], data['member'])
	return jsonify({'message': response}), 200

@app.route('/unblock_member', methods=['POST'])
def unblock_member():
	data = request.get_json()
	response = group.unblock_member(data['group_name'], data['member'])
	return jsonify({'message': response}), 200

if __name__ == '__main__':
	app.run(debug=True)
