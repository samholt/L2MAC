from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
	return jsonify(users)

@app.route('/signup', methods=['POST'])
def signup():
	user_id = str(len(users) + 1)
	user_data = request.get_json()
	users[user_id] = user_data
	response = make_response(jsonify({'message': 'User registered successfully', 'user_id': user_id}), 201)
	return response

@app.route('/password_recovery/<user_id>', methods=['GET'])
def password_recovery(user_id):
	if user_id in users:
		print('Password reset link has been sent to the email of user with ID: ' + user_id)
		response = make_response(jsonify({'message': 'Password reset link sent'}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/set_profile_picture/<user_id>', methods=['POST'])
def set_profile_picture(user_id):
	if user_id in users:
		new_picture = request.get_json().get('new_picture', '')
		users[user_id]['profile_picture'] = new_picture
		response = make_response(jsonify({'message': 'Profile picture updated'}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/set_status_message/<user_id>', methods=['POST'])
def set_status_message(user_id):
	if user_id in users:
		new_message = request.get_json().get('new_message', '')
		users[user_id]['status_message'] = new_message
		response = make_response(jsonify({'message': 'Status message updated'}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/update_privacy_settings/<user_id>', methods=['POST'])
def update_privacy_settings(user_id):
	if user_id in users:
		new_settings = request.get_json().get('new_settings', {})
		users[user_id]['privacy_settings'] = new_settings
		response = make_response(jsonify({'message': 'Privacy settings updated'}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/block_contact/<user_id>', methods=['POST'])
def block_contact(user_id):
	if user_id in users:
		contact_id = request.get_json().get('contact_id', '')
		if contact_id not in users[user_id]['blocked_contacts']:
			users[user_id]['blocked_contacts'].append(contact_id)
			response = make_response(jsonify({'message': 'Contact blocked'}), 200)
		else:
			response = make_response(jsonify({'message': 'Contact already blocked'}), 400)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/unblock_contact/<user_id>', methods=['POST'])
def unblock_contact(user_id):
	if user_id in users:
		contact_id = request.get_json().get('contact_id', '')
		if contact_id in users[user_id]['blocked_contacts']:
			users[user_id]['blocked_contacts'].remove(contact_id)
			response = make_response(jsonify({'message': 'Contact unblocked'}), 200)
		else:
			response = make_response(jsonify({'message': 'Contact not blocked'}), 400)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/manage_group/<user_id>', methods=['POST'])
def manage_group(user_id):
	if user_id in users:
		group_details = request.get_json().get('group_details', {})
		group_id = group_details.get('group_id', '')
		if group_id:
			for group in users[user_id]['groups']:
				if group['group_id'] == group_id:
					group.update(group_details)
					break
			else:
				users[user_id]['groups'].append(group_details)
		response = make_response(jsonify({'message': 'Group managed'}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/send_message/<user_id>', methods=['POST'])
def send_message(user_id):
	if user_id in users:
		message_details = request.get_json()
		recipient_id = message_details.get('recipient_id', '')
		message = message_details.get('message', '')
		if recipient_id in users:
			message_id = str(len(users[user_id]['messages']) + 1)
			users[user_id]['messages'].append({'message_id': message_id, 'message': message, 'recipient_id': recipient_id, 'read': False})
			response = make_response(jsonify({'message': 'Message sent', 'message_id': message_id}), 200)
		else:
			response = make_response(jsonify({'message': 'Recipient not found'}), 404)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/read_message/<user_id>', methods=['POST'])
def read_message(user_id):
	if user_id in users:
		message_id = request.get_json().get('message_id', '')
		for message in users[user_id]['messages']:
			if message['message_id'] == message_id:
				message['read'] = True
				response = make_response(jsonify({'message': 'Message marked as read'}), 200)
				break
		else:
			response = make_response(jsonify({'message': 'Message not found'}), 404)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/share_image/<user_id>', methods=['POST'])
def share_image(user_id):
	if user_id in users:
		image_details = request.get_json()
		recipient_id = image_details.get('recipient_id', '')
		image = image_details.get('image', '')
		if recipient_id in users:
			image_id = str(len(users[user_id]['images']) + 1)
			users[user_id]['images'].append({'image_id': image_id, 'image': image, 'recipient_id': recipient_id})
			response = make_response(jsonify({'message': 'Image shared', 'image_id': image_id}), 200)
		else:
			response = make_response(jsonify({'message': 'Recipient not found'}), 404)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/post_status/<user_id>', methods=['POST'])
def post_status(user_id):
	if user_id in users:
		status_details = request.get_json()
		status_id = str(len(users[user_id]['statuses']) + 1)
		users[user_id]['statuses'].append({'status_id': status_id, 'status_details': status_details})
		response = make_response(jsonify({'message': 'Status posted', 'status_id': status_id}), 200)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

@app.route('/update_status_visibility/<user_id>', methods=['POST'])
def update_status_visibility(user_id):
	if user_id in users:
		status_id = request.get_json().get('status_id', '')
		visibility = request.get_json().get('visibility', '')
		for status in users[user_id]['statuses']:
			if status['status_id'] == status_id:
				status['visibility'] = visibility
				response = make_response(jsonify({'message': 'Status visibility updated'}), 200)
				break
		else:
			response = make_response(jsonify({'message': 'Status not found'}), 404)
		return response
	else:
		response = make_response(jsonify({'message': 'User not found'}), 404)
		return response

if __name__ == '__main__':
	app.run(debug=True)
