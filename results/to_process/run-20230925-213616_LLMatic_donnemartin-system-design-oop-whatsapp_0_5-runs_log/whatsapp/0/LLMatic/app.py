from flask import Flask, request, jsonify
from auth import register_user, recover_password, set_profile_picture, set_status_message, set_privacy_settings
from contacts import block_unblock_contact, create_group, edit_group
from messages import send_message, read_message, update_read_receipt, encrypt_message, share_image, create_group_chat, add_participant, remove_participant, set_admin
from status import post_status

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = register_user(data['email'], data['password'])
	return jsonify(user), 201

@app.route('/recover', methods=['POST'])
def recover():
	data = request.get_json()
	password = recover_password(data['email'])
	return jsonify({'password': password}), 200

@app.route('/profile_picture', methods=['POST'])
def profile_picture():
	data = request.get_json()
	set_profile_picture(data['email'], data['picture'])
	return jsonify({'message': 'Profile picture set.'}), 200

@app.route('/status_message', methods=['POST'])
def status_message():
	data = request.get_json()
	set_status_message(data['email'], data['message'])
	return jsonify({'message': 'Status message set.'}), 200

@app.route('/privacy_settings', methods=['POST'])
def privacy_settings():
	data = request.get_json()
	set_privacy_settings(data['email'], data['settings'])
	return jsonify({'message': 'Privacy settings set.'}), 200

@app.route('/block_unblock', methods=['POST'])
def block_unblock():
	data = request.get_json()
	block_unblock_contact(data['user_email'], data['contact_email'])
	return jsonify({'message': 'Contact blocked/unblocked.'}), 200

@app.route('/create_group', methods=['POST'])
def create_group_route():
	data = request.get_json()
	create_group(data['group_name'], data['user_email'])
	return jsonify({'message': 'Group created.'}), 201

@app.route('/edit_group', methods=['POST'])
def edit_group_route():
	data = request.get_json()
	edit_group(data['group_name'], data['user_email'], data['action'])
	return jsonify({'message': 'Group edited.'}), 200

@app.route('/send_message', methods=['POST'])
def send_message_route():
	data = request.get_json()
	send_message(data['sender'], data['recipient'], data['content'], data.get('group_chat'))
	return jsonify({'message': 'Message sent.'}), 201

@app.route('/read_message', methods=['POST'])
def read_message_route():
	data = request.get_json()
	message = read_message(data['sender'], data['recipient'])
	return jsonify(message), 200

@app.route('/update_read_receipt', methods=['POST'])
def update_read_receipt_route():
	data = request.get_json()
	update_read_receipt(data['sender'], data['recipient'])
	return jsonify({'message': 'Read receipt updated.'}), 200

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message_route():
	data = request.get_json()
	encrypt_message(data['sender'], data['recipient'])
	return jsonify({'message': 'Message encrypted.'}), 200

@app.route('/share_image', methods=['POST'])
def share_image_route():
	data = request.get_json()
	share_image(data['sender'], data['recipient'], data['image_content'])
	return jsonify({'message': 'Image shared.'}), 201

@app.route('/create_group_chat', methods=['POST'])
def create_group_chat_route():
	data = request.get_json()
	create_group_chat(data['name'], data['participants'])
	return jsonify({'message': 'Group chat created.'}), 201

@app.route('/add_participant', methods=['POST'])
def add_participant_route():
	data = request.get_json()
	add_participant(data['group_chat'], data['participant'])
	return jsonify({'message': 'Participant added.'}), 200

@app.route('/remove_participant', methods=['POST'])
def remove_participant_route():
	data = request.get_json()
	remove_participant(data['group_chat'], data['participant'])
	return jsonify({'message': 'Participant removed.'}), 200

@app.route('/set_admin', methods=['POST'])
def set_admin_route():
	data = request.get_json()
	set_admin(data['group_chat'], data['admin'])
	return jsonify({'message': 'Admin set.'}), 200

@app.route('/post_status', methods=['POST'])
def post_status_route():
	data = request.get_json()
	status = post_status(data['email'], data['content'], data['visibility'])
	return jsonify(status), 201

if __name__ == '__main__':
	app.run(debug=True)
