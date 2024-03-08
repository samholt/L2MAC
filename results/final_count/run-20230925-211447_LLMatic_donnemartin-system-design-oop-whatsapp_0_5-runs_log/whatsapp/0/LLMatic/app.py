from flask import Flask, request
from auth import signup, login, generate_password_reset_link, reset_password
from profile import UserProfile
from contacts import Contacts
from messaging import Messaging
from status import post_status, update_visibility

app = Flask(__name__)

user_profile = UserProfile()
contacts = Contacts()
messaging = Messaging()

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/signup', methods=['POST'])
def signup_route():
	data = request.get_json()
	return signup(data['email'], data['password'])

@app.route('/login', methods=['POST'])
def login_route():
	data = request.get_json()
	return login(data['email'], data['password'])

@app.route('/reset_password', methods=['POST'])
def reset_password_route():
	data = request.get_json()
	return reset_password(data['token'], data['new_password'])

@app.route('/profile/picture', methods=['POST'])
def set_profile_picture_route():
	data = request.get_json()
	user_profile.set_profile_picture(data['email'], data['picture'])
	return 'Profile picture updated'

@app.route('/profile/status', methods=['POST'])
def set_status_message_route():
	data = request.get_json()
	user_profile.set_status_message(data['email'], data['status'])
	return 'Status message updated'

@app.route('/profile/privacy', methods=['POST'])
def set_privacy_settings_route():
	data = request.get_json()
	user_profile.set_privacy_settings(data['email'], data['privacy'])
	return 'Privacy settings updated'

@app.route('/contacts/block', methods=['POST'])
def block_unblock_contact_route():
	data = request.get_json()
	contacts.block_unblock_contact(data['user_email'], data['contact_email'])
	return 'Contact block status updated'

@app.route('/contacts/group', methods=['POST'])
def manage_group_route():
	data = request.get_json()
	contacts.manage_group(data['user_email'], data['group_name'], data['emails'])
	return 'Group updated'

@app.route('/messaging/send', methods=['POST'])
def send_message_route():
	data = request.get_json()
	messaging.send_message(data['sender_email'], data['receiver_email'], data['message'])
	return 'Message sent'

@app.route('/messaging/read', methods=['POST'])
def read_message_route():
	data = request.get_json()
	messaging.read_message(data['sender_email'], data['receiver_email'], data['message_id'])
	return 'Message read'

@app.route('/messaging/group', methods=['POST'])
def create_group_chat_route():
	data = request.get_json()
	messaging.create_group_chat(data['user_email'], data['group_name'], data['picture'], data['emails'])
	return 'Group chat created'

@app.route('/status/post', methods=['POST'])
def post_status_route():
	data = request.get_json()
	return post_status(data['email'], data['image'], data['visibility'])

@app.route('/status/update_visibility', methods=['POST'])
def update_visibility_route():
	data = request.get_json()
	return str(update_visibility(data['email'], data['status_id'], data['visibility_emails']))

if __name__ == '__main__':
	app.run(debug=True)
