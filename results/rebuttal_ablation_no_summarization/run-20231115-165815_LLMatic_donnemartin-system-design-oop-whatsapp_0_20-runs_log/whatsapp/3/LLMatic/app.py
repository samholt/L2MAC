from flask import Flask, request, render_template
from models.user import User
from models.group import Group
from models.message import Message
from models.status import Status
import hashlib

app = Flask(__name__)

# Mock database
users_db = {'test1@test.com': User('test1@test.com', 'password', '', '', ''), 'test2@test.com': User('test2@test.com', 'password', '', '', '')}
groups_db = {}
messages_db = {}
statuses_db = {}

# Mock message queue
message_queue = {}

# Mock online status
online_status = {}

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		if email in users_db:
			return {'message': 'User already exists'}, 400
		user = User(email, password, '', '', '')
		users_db[email] = user
		return {'message': 'User created successfully'}, 201
	else:
		return render_template('signup.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
	if request.method == 'POST':
		email = request.form.get('email')
		if email not in users_db:
			return {'message': 'User does not exist'}, 400
		# In a real application, generate a password reset link and send it to the user's email.
		# For this task, we just return a success message.
		return {'message': 'Password reset link sent'}, 200
	else:
		return render_template('forgot_password.html')

@app.route('/set_profile_picture', methods=['GET', 'POST'])
def set_profile_picture():
	if request.method == 'POST':
		email = request.form.get('email')
		profile_picture = request.form.get('profile_picture')
		if email not in users_db:
			return {'message': 'User does not exist'}, 400
		users_db[email].profile_picture = profile_picture
		return {'message': 'Profile picture updated successfully'}, 200
	else:
		return render_template('set_profile_picture.html')

@app.route('/set_status_message', methods=['GET', 'POST'])
def set_status_message():
	if request.method == 'POST':
		email = request.form.get('email')
		status_message = request.form.get('status_message')
		if email not in users_db:
			return {'message': 'User does not exist'}, 400
		users_db[email].status_message = status_message
		return {'message': 'Status message updated successfully'}, 200
	else:
		return render_template('set_status_message.html')

@app.route('/set_privacy_settings', methods=['GET', 'POST'])
def set_privacy_settings():
	if request.method == 'POST':
		email = request.form.get('email')
		privacy_settings = request.form.get('privacy_settings')
		if email not in users_db:
			return {'message': 'User does not exist'}, 400
		users_db[email].privacy_settings = privacy_settings
		return {'message': 'Privacy settings updated successfully'}, 200
	else:
		return render_template('set_privacy_settings.html')

@app.route('/block_user', methods=['GET', 'POST'])
def block_user():
	if request.method == 'POST':
		user_email = request.form.get('user_email')
		blocked_user_email = request.form.get('blocked_user_email')
		if user_email not in users_db or blocked_user_email not in users_db:
			return {'message': 'User does not exist'}, 400
		users_db[user_email].blocked_users.append(blocked_user_email)
		return {'message': 'User blocked successfully'}, 200
	else:
		return render_template('block_user.html')

@app.route('/unblock_user', methods=['GET', 'POST'])
def unblock_user():
	if request.method == 'POST':
		user_email = request.form.get('user_email')
		unblocked_user_email = request.form.get('unblocked_user_email')
		if user_email not in users_db or unblocked_user_email not in users_db:
			return {'message': 'User does not exist'}, 400
		users_db[user_email].blocked_users.remove(unblocked_user_email)
		return {'message': 'User unblocked successfully'}, 200
	else:
		return render_template('unblock_user.html')

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
	if request.method == 'POST':
		group_name = request.form.get('group_name')
		group_picture = request.form.get('group_picture')
		participants = request.form.get('participants')
		admin_roles = request.form.get('admin_roles')
		if group_name in groups_db:
			return {'message': 'Group already exists'}, 400
		group = Group(group_name, group_picture, participants, admin_roles)
		groups_db[group_name] = group
		return {'message': 'Group created successfully'}, 201
	else:
		return render_template('create_group.html')

@app.route('/edit_group', methods=['GET', 'POST'])
def edit_group():
	if request.method == 'POST':
		group_name = request.form.get('group_name')
		new_group_name = request.form.get('new_group_name')
		group_picture = request.form.get('group_picture')
		participants = request.form.get('participants')
		admin_roles = request.form.get('admin_roles')
		if group_name not in groups_db:
			return {'message': 'Group does not exist'}, 400
		group = groups_db.pop(group_name)
		group.name = new_group_name
		group.picture = group_picture
		group.participants = participants
		group.admin_roles = admin_roles
		groups_db[new_group_name] = group
		return {'message': 'Group edited successfully'}, 200
	else:
		return render_template('edit_group.html')

@app.route('/add_participant', methods=['GET', 'POST'])
def add_participant():
	if request.method == 'POST':
		group_name = request.form.get('group_name')
		user_email = request.form.get('user_email')
		if group_name not in groups_db or user_email not in users_db:
			return {'message': 'Group or user does not exist'}, 400
		groups_db[group_name].participants.append(user_email)
		return {'message': 'Participant added successfully'}, 200
	else:
		return render_template('add_participant.html')

@app.route('/remove_participant', methods=['GET', 'POST'])
def remove_participant():
	if request.method == 'POST':
		group_name = request.form.get('group_name')
		user_email = request.form.get('user_email')
		if group_name not in groups_db or user_email not in users_db:
			return {'message': 'Group or user does not exist'}, 400
		groups_db[group_name].participants.remove(user_email)
		return {'message': 'Participant removed successfully'}, 200
	else:
		return render_template('remove_participant.html')

@app.route('/update_admin_role', methods=['GET', 'POST'])
def update_admin_role():
	if request.method == 'POST':
		group_name = request.form.get('group_name')
		user_email = request.form.get('user_email')
		role = request.form.get('role')
		if group_name not in groups_db or user_email not in users_db:
			return {'message': 'Group or user does not exist'}, 400
		groups_db[group_name].admin_roles[user_email] = role
		return {'message': 'Admin role updated successfully'}, 200
	else:
		return render_template('update_admin_role.html')

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
	if request.method == 'POST':
		sender = request.form.get('sender')
		receiver = request.form.get('receiver')
		content = request.form.get('content')
		if online_status.get(receiver, False):
			message = Message(sender, receiver, content, False, False, '')
			messages_db[message.id] = message
			return {'message': 'Message sent successfully'}, 201
		else:
			message_queue.setdefault(receiver, []).append((sender, content))
			return {'message': 'User is offline. Message queued.'}, 200
	else:
		return render_template('send_message.html')

@app.route('/read_message', methods=['GET', 'POST'])
def read_message():
	if request.method == 'POST':
		message_id = request.form.get('message_id')
		if message_id not in messages_db:
			return {'message': 'Message does not exist'}, 400
		messages_db[message_id].read_receipt = True
		return {'message': 'Read receipt updated successfully'}, 200
	else:
		return render_template('read_message.html')

@app.route('/encrypt_message', methods=['GET', 'POST'])
def encrypt_message():
	if request.method == 'POST':
		message_id = request.form.get('message_id')
		if message_id not in messages_db:
			return {'message': 'Message does not exist'}, 400
		message = messages_db[message_id]
		message.content = hashlib.sha256(message.content.encode()).hexdigest()
		message.encryption = True
		return {'message': 'Message encrypted successfully'}, 200
	else:
		return render_template('encrypt_message.html')

@app.route('/share_image', methods=['GET', 'POST'])
def share_image():
	if request.method == 'POST':
		message_id = request.form.get('message_id')
		image = request.form.get('image')
		if message_id not in messages_db:
			return {'message': 'Message does not exist'}, 400
		messages_db[message_id].image = image
		return {'message': 'Image shared successfully'}, 200
	else:
		return render_template('share_image.html')

@app.route('/post_status', methods=['GET', 'POST'])
def post_status():
	if request.method == 'POST':
		user_id = request.form.get('user_id')
		content = request.form.get('content')
		time_limit = request.form.get('time_limit')
		status = Status(user_id, content, True, time_limit)
		statuses_db[status.id] = status
		return {'message': 'Status posted successfully'}, 201
	else:
		return render_template('post_status.html')

@app.route('/update_status_visibility', methods=['GET', 'POST'])
def update_status_visibility():
	if request.method == 'POST':
		status_id = request.form.get('status_id')
		visibility = request.form.get('visibility')
		if status_id not in statuses_db:
			return {'message': 'Status does not exist'}, 400
		statuses_db[status_id].visibility = visibility
		return {'message': 'Status visibility updated successfully'}, 200
	else:
		return render_template('update_status_visibility.html')

@app.route('/online_status', methods=['GET'])
def online_status():
	user_id = request.args.get('user_id')
	if user_id not in users_db:
		return {'message': 'User does not exist'}, 400
	return {'online': online_status.get(user_id, False)}

if __name__ == '__main__':
	app.run(debug=True)
