from flask import Flask, request
from services.user_service import UserService
from services.message_service import MessageService
from services.group_service import GroupService
from services.status_service import StatusService

app = Flask(__name__)

user_service = UserService()
message_service = MessageService()
group_service = GroupService()
status_service = StatusService()

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return {'success': user_service.register(data['email'], data['password'])}

@app.route('/authenticate', methods=['POST'])
def authenticate():
	data = request.get_json()
	return {'success': user_service.authenticate(data['email'], data['password'])}

@app.route('/set_profile', methods=['POST'])
def set_profile():
	data = request.get_json()
	return {'success': user_service.set_profile(data['email'], data['picture'], data['status'])}

@app.route('/set_privacy', methods=['POST'])
def set_privacy():
	data = request.get_json()
	return {'success': user_service.set_privacy(data['email'], data['privacy'])}

@app.route('/block_contact', methods=['POST'])
def block_contact():
	data = request.get_json()
	return {'success': user_service.block_contact(data['email'], data['contact'])}

@app.route('/unblock_contact', methods=['POST'])
def unblock_contact():
	data = request.get_json()
	return {'success': user_service.unblock_contact(data['email'], data['contact'])}

@app.route('/send_message', methods=['POST'])
def send_message():
	data = request.get_json()
	message_service.send_message(data['id'], data['sender'], data['receiver'], data['content'])
	return {'success': True}

@app.route('/receive_message/<id>', methods=['GET'])
def receive_message(id):
	return {'message': message_service.receive_message(id).to_dict()}

@app.route('/set_read_receipt', methods=['POST'])
def set_read_receipt():
	data = request.get_json()
	message_service.set_read_receipt(data['id'])
	return {'success': True}

@app.route('/encrypt_message', methods=['POST'])
def encrypt_message():
	data = request.get_json()
	message_service.encrypt_message(data['id'])
	return {'success': True}

@app.route('/share_image', methods=['POST'])
def share_image():
	data = request.get_json()
	message_service.share_image(data['id'], data['image'])
	return {'success': True}

@app.route('/create_group', methods=['POST'])
def create_group():
	data = request.get_json()
	return {'group': group_service.create_group(data['group_id'], data['group_name'])}

@app.route('/add_participant', methods=['POST'])
def add_participant():
	data = request.get_json()
	return {'group': group_service.add_participant(data['group_id'], data['user_id'])}

@app.route('/remove_participant', methods=['POST'])
def remove_participant():
	data = request.get_json()
	return {'group': group_service.remove_participant(data['group_id'], data['user_id'])}

@app.route('/set_admin', methods=['POST'])
def set_admin():
	data = request.get_json()
	return {'group': group_service.set_admin(data['group_id'], data['user_id'])}

@app.route('/post_status', methods=['POST'])
def post_status():
	data = request.get_json()
	return {'status': status_service.post_status(data['id'], data['user'], data['image'], data['visibility'], data['time_limit']).to_dict()}

@app.route('/set_visibility', methods=['POST'])
def set_visibility():
	data = request.get_json()
	return {'status': status_service.set_visibility(data['id'], data['visibility']).to_dict()}

@app.route('/set_time_limit', methods=['POST'])
def set_time_limit():
	data = request.get_json()
	return {'status': status_service.set_time_limit(data['id'], data['time_limit']).to_dict()}

if __name__ == '__main__':
	app.run(debug=True)
