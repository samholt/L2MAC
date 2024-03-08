from flask import Flask, request
from user import User
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

user = User()
message = Message()
group = Group()
status = Status()

@app.route('/sign_up', methods=['POST'])
def sign_up():
	email = request.form.get('email')
	password = request.form.get('password')
	return user.sign_up(email, password)

@app.route('/forgotten_password', methods=['POST'])
def forgotten_password():
	email = request.form.get('email')
	return user.forgotten_password(email)

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	user_id = request.form.get('user_id')
	image_file = request.form.get('image_file')
	return user.set_profile_picture(user_id, image_file)

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	user_id = request.form.get('user_id')
	status_message = request.form.get('status_message')
	return user.set_status_message(user_id, status_message)

@app.route('/set_privacy_settings', methods=['POST'])
def set_privacy_settings():
	user_id = request.form.get('user_id')
	privacy_setting = request.form.get('privacy_setting')
	return user.set_privacy_settings(user_id, privacy_setting)

@app.route('/block_contact', methods=['POST'])
def block_contact():
	user_id = request.form.get('user_id')
	contact_id = request.form.get('contact_id')
	return user.block_contact(user_id, contact_id)

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	user_id = request.form.get('user_id')
	contact_id = request.form.get('contact_id')
	return user.unblock_contact(user_id, contact_id)

@app.route('/set_online_status', methods=['POST'])
def set_online_status():
	user_id = request.form.get('user_id')
	status = request.form.get('status')
	return user.set_online_status(user_id, status)

@app.route('/get_online_status', methods=['POST'])
def get_online_status():
	user_id = request.form.get('user_id')
	return user.get_online_status(user_id)

@app.route('/send_message', methods=['POST'])
def send_message():
	sender_id = request.form.get('sender_id')
	receiver_id = request.form.get('receiver_id')
	message_text = request.form.get('message_text')
	return message.send_message(sender_id, receiver_id, message_text)

@app.route('/receive_message', methods=['POST'])
def receive_message():
	receiver_id = request.form.get('receiver_id')
	return message.receive_message(receiver_id)

@app.route('/send_read_receipt', methods=['POST'])
def send_read_receipt():
	sender_id = request.form.get('sender_id')
	receiver_id = request.form.get('receiver_id')
	message_id = request.form.get('message_id')
	return message.send_read_receipt(sender_id, receiver_id, message_id)

@app.route('/share_image', methods=['POST'])
def share_image():
	sender_id = request.form.get('sender_id')
	receiver_id = request.form.get('receiver_id')
	image_file = request.form.get('image_file')
	return message.share_image(sender_id, receiver_id, image_file)

@app.route('/queue_offline_message', methods=['POST'])
def queue_offline_message():
	sender_id = request.form.get('sender_id')
	receiver_id = request.form.get('receiver_id')
	message_text = request.form.get('message_text')
	return message.queue_offline_message(sender_id, receiver_id, message_text)

@app.route('/get_offline_messages', methods=['POST'])
def get_offline_messages():
	receiver_id = request.form.get('receiver_id')
	return message.get_offline_messages(receiver_id)

@app.route('/create_group', methods=['POST'])
def create_group():
	user_id = request.form.get('user_id')
	group_name = request.form.get('group_name')
	member_ids = request.form.get('member_ids')
	return group.create_group(user_id, group_name, member_ids)

@app.route('/edit_group', methods=['POST'])
def edit_group():
	user_id = request.form.get('user_id')
	old_group_name = request.form.get('old_group_name')
	new_group_name = request.form.get('new_group_name')
	new_member_ids = request.form.get('new_member_ids')
	return group.edit_group(user_id, old_group_name, new_group_name, new_member_ids)

@app.route('/manage_groups', methods=['POST'])
def manage_groups():
	user_id = request.form.get('user_id')
	return group.manage_groups(user_id)

@app.route('/add_participant', methods=['POST'])
def add_participant():
	user_id = request.form.get('user_id')
	group_name = request.form.get('group_name')
	participant_id = request.form.get('participant_id')
	return group.add_participant(user_id, group_name, participant_id)

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	user_id = request.form.get('user_id')
	group_name = request.form.get('group_name')
	participant_id = request.form.get('participant_id')
	return group.remove_participant(user_id, group_name, participant_id)

@app.route('/manage_admin_roles', methods=['POST'])
def manage_admin_roles():
	user_id = request.form.get('user_id')
	group_name = request.form.get('group_name')
	role = request.form.get('role')
	return group.manage_admin_roles(user_id, group_name, role)

@app.route('/post_status', methods=['POST'])
def post_status():
	user_id = request.form.get('user_id')
	image_file = request.form.get('image_file')
	visibility = request.form.get('visibility')
	return status.post_status(user_id, image_file, visibility)

@app.route('/control_visibility', methods=['POST'])
def control_visibility():
	user_id = request.form.get('user_id')
	status_id = request.form.get('status_id')
	visibility = request.form.get('visibility')
	return status.control_visibility(user_id, status_id, visibility)

if __name__ == '__main__':
	app.run(debug=True)
