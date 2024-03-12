from flask import Flask, render_template, request
from user import User, Contact
from message import Message
from group import Group
from status import Status

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/sign_up', methods=['POST'])
def sign_up():
	email = request.form.get('email')
	password = request.form.get('password')
	user = User(email, password)
	return user.sign_up(email, password)

@app.route('/password_recovery', methods=['POST'])
def password_recovery():
	email = request.form.get('email')
	user = User(email, '')
	return user.password_recovery(email)

@app.route('/set_profile_picture', methods=['POST'])
def set_profile_picture():
	picture_file = request.form.get('picture_file')
	user = User('', '')
	return user.set_profile_picture(picture_file)

@app.route('/set_status_message', methods=['POST'])
def set_status_message():
	status_message = request.form.get('status_message')
	user = User('', '')
	return user.set_status_message(status_message)

@app.route('/manage_privacy_settings', methods=['POST'])
def manage_privacy_settings():
	privacy_settings = request.form.get('privacy_settings')
	user = User('', '')
	return user.manage_privacy_settings(privacy_settings)

@app.route('/block_contact', methods=['POST'])
def block_contact():
	user = request.form.get('user')
	contact = Contact(user)
	return contact.block_contact(user)

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	user = request.form.get('user')
	contact = Contact(user)
	return contact.unblock_contact(user)

@app.route('/create_group', methods=['POST'])
def create_group():
	group_details = request.form.get('group_details')
	contact = Contact('')
	return contact.create_group(group_details)

@app.route('/edit_group', methods=['POST'])
def edit_group():
	group_details = request.form.get('group_details')
	contact = Contact('')
	return contact.edit_group(group_details)

@app.route('/manage_group', methods=['POST'])
def manage_group():
	group_details = request.form.get('group_details')
	contact = Contact('')
	return contact.manage_group(group_details)

@app.route('/send_message', methods=['POST'])
def send_message():
	receiver = request.form.get('receiver')
	text = request.form.get('text')
	message = Message('', receiver, text, '', '', '')
	message.send_message(receiver, text)
	return 'Message sent'

@app.route('/receive_message', methods=['POST'])
def receive_message():
	sender = request.form.get('sender')
	text = request.form.get('text')
	message = Message(sender, '', text, '', '', '')
	message.receive_message(sender, text)
	return 'Message received'

@app.route('/manage_read_receipt', methods=['POST'])
def manage_read_receipt():
	read_receipt = request.form.get('read_receipt')
	message = Message('', '', '', read_receipt, '', '')
	message.manage_read_receipt(read_receipt)
	return 'Read receipt managed'

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message():
	text = request.form.get('text')
	encryption_key = request.form.get('encryption_key')
	message = Message('', '', text, '', encryption_key, '')
	message.encrypt_message(text, encryption_key)
	return 'Message encrypted'

@app.route('/decrypt_message', methods=['POST'])
def decrypt_message():
	encrypted_text = request.form.get('encrypted_text')
	encryption_key = request.form.get('encryption_key')
	message = Message('', '', '', '', encryption_key, '')
	message.decrypt_message(encrypted_text, encryption_key)
	return 'Message decrypted'

@app.route('/share_image', methods=['POST'])
def share_image():
	image = request.form.get('image')
	message = Message('', '', '', '', '', image)
	message.share_image(image)
	return 'Image shared'

@app.route('/post_image_status', methods=['POST'])
def post_image_status():
	image = request.form.get('image')
	visibility_time = request.form.get('visibility_time')
	status = Status('', image, visibility_time, '')
	status.post_image_status(image, visibility_time)
	return 'Image status posted'

@app.route('/manage_viewers', methods=['POST'])
def manage_viewers():
	viewers = request.form.get('viewers')
	status = Status('', '', '', viewers)
	status.manage_viewers(viewers)
	return 'Viewers managed'

if __name__ == '__main__':
	app.run(debug=True)
