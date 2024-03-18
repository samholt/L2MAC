from flask import Flask, request, jsonify
import mock_db

app = Flask(__name__)
db = mock_db.MockDB()

@app.route('/', methods=['GET'])
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	if 'email' not in data or 'password' not in data:
		return jsonify({'message': 'Missing email or password'}), 400
	db.add_user(data['email'], data['password'])
	return jsonify({'message': 'User registered successfully'}), 200

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	if 'email' not in data:
		return jsonify({'message': 'Missing email'}), 400
	user = db.get_user(data['email'])
	if user is None:
		return jsonify({'message': 'User not found'}), 404
	return jsonify({'message': 'Password reset link has been sent to your email'}), 200

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	data = request.get_json()
	if 'user_id' not in data or 'picture' not in data:
		return jsonify({'message': 'Missing user_id or picture'}), 400
	db.update_user_picture(data['user_id'], data['picture'])
	return jsonify({'message': 'Profile picture updated successfully'}), 200

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	data = request.get_json()
	if 'user_id' not in data or 'message' not in data:
		return jsonify({'message': 'Missing user_id or message'}), 400
	db.update_user_status_message(data['user_id'], data['message'])
	return jsonify({'message': 'Status message updated successfully'}), 200

@app.route('/update_privacy_settings', methods=['POST'])
def update_privacy_settings():
	data = request.get_json()
	if 'user_id' not in data or 'settings' not in data:
		return jsonify({'message': 'Missing user_id or settings'}), 400
	db.update_user_privacy_settings(data['user_id'], data['settings'])
	return jsonify({'message': 'Privacy settings updated successfully'}), 200

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	if 'user_id' not in data or 'contact_id' not in data:
		return jsonify({'message': 'Missing user_id or contact_id'}), 400
	db.block_contact(data['user_id'], data['contact_id'])
	return jsonify({'message': 'Contact blocked successfully'}), 200

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	if 'user_id' not in data or 'contact_id' not in data:
		return jsonify({'message': 'Missing user_id or contact_id'}), 400
	db.unblock_contact(data['user_id'], data['contact_id'])
	return jsonify({'message': 'Contact unblocked successfully'}), 200

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	if 'user_id' not in data or 'group_details' not in data:
		return jsonify({'message': 'Missing user_id or group_details'}), 400
	db.create_group(data['user_id'], data['group_details'])
	return jsonify({'message': 'Group created successfully'}), 200

@app.route('/edit_group', methods=['POST'])
def edit_group():
	data = request.get_json()
	if 'user_id' not in data or 'group_id' not in data or 'group_details' not in data:
		return jsonify({'message': 'Missing user_id, group_id or group_details'}), 400
	db.edit_group(data['user_id'], data['group_id'], data['group_details'])
	return jsonify({'message': 'Group edited successfully'}), 200

@app.route('/delete_group', methods=['POST'])
def delete_group():
	data = request.get_json()
	if 'user_id' not in data or 'group_id' not in data:
		return jsonify({'message': 'Missing user_id or group_id'}), 400
	db.delete_group(data['user_id'], data['group_id'])
	return jsonify({'message': 'Group deleted successfully'}), 200

@app.route('/add_participant', methods=['POST'])
def add_participant():
	data = request.get_json()
	if 'group_id' not in data or 'participant_id' not in data:
		return jsonify({'message': 'Missing group_id or participant_id'}), 400
	db.add_participant(data['group_id'], data['participant_id'])
	return jsonify({'message': 'Participant added successfully'}), 200

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	data = request.get_json()
	if 'group_id' not in data or 'participant_id' not in data:
		return jsonify({'message': 'Missing group_id or participant_id'}), 400
	db.remove_participant(data['group_id'], data['participant_id'])
	return jsonify({'message': 'Participant removed successfully'}), 200

@app.route('/add_admin', methods=['POST'])
def add_admin():
	data = request.get_json()
	if 'group_id' not in data or 'admin_id' not in data:
		return jsonify({'message': 'Missing group_id or admin_id'}), 400
	db.add_admin(data['group_id'], data['admin_id'])
	return jsonify({'message': 'Admin added successfully'}), 200

@app.route('/remove_admin', methods=['POST'])
def remove_admin():
	data = request.get_json()
	if 'group_id' not in data or 'admin_id' not in data:
		return jsonify({'message': 'Missing group_id or admin_id'}), 400
	db.remove_admin(data['group_id'], data['admin_id'])
	return jsonify({'message': 'Admin removed successfully'}), 200

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	if 'sender_id' not in data or 'receiver_id' not in data or 'message' not in data:
		return jsonify({'message': 'Missing sender_id, receiver_id or message'}), 400
	db.send_message(data['sender_id'], data['receiver_id'], data['message'])
	return jsonify({'message': 'Message sent successfully'}), 200

@app.route('/read_message', methods=['POST'])
def read_message():
	data = request.get_json()
	if 'user_id' not in data or 'message_id' not in data:
		return jsonify({'message': 'Missing user_id or message_id'}), 400
	db.read_message(data['user_id'], data['message_id'])
	return jsonify({'message': 'Message marked as read'}), 200

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message():
	data = request.get_json()
	if 'user_id' not in data or 'message_id' not in data or 'encryption_key' not in data:
		return jsonify({'message': 'Missing user_id, message_id or encryption_key'}), 400
	db.encrypt_message(data['user_id'], data['message_id'], data['encryption_key'])
	return jsonify({'message': 'Message encrypted successfully'}), 200

@app.route('/share_content', methods=['POST'])
def share_content():
	data = request.get_json()
	if 'user_id' not in data or 'receiver_id' not in data or 'content' not in data:
		return jsonify({'message': 'Missing user_id, receiver_id or content'}), 400
	db.share_content(data['user_id'], data['receiver_id'], data['content'])
	return jsonify({'message': 'Content shared successfully'}), 200

if __name__ == '__main__':
	app.run(debug=True)
