from flask import Flask, request
from user import register, login, forgot_password, profile, change_password
from file import upload, download
from share import Share
from security import Security
from ui import UI

app = Flask(__name__)
share = Share()
security = Security()
ui = UI()

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	return register(data['name'], data['email'], data['password'])

@app.route('/login', methods=['POST'])
def login_user():
	data = request.get_json()
	return login(data['email'], data['password'])

@app.route('/forgot_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	return forgot_password(data['email'])

@app.route('/profile', methods=['GET'])
def get_profile():
	data = request.get_json()
	return profile(data['email'])

@app.route('/change_password', methods=['POST'])
def update_password():
	data = request.get_json()
	return change_password(data['email'], data['old_password'], data['new_password'])

@app.route('/upload', methods=['POST'])
def upload_file():
	data = request.get_json()
	return upload(data['file'], data['email'])

@app.route('/download', methods=['GET'])
def download_file():
	data = request.get_json()
	return download(data['file_name'], data['email'], data['version_number'])

@app.route('/share', methods=['POST'])
def share_file():
	data = request.get_json()
	return share.generate_shareable_link(data['file_path'], data['expiry_date'], data['password'])

@app.route('/get_shared_file', methods=['GET'])
def get_shared_file():
	data = request.get_json()
	return share.get_shared_file(data['share_id'], data['password'])

@app.route('/encrypt', methods=['POST'])
def encrypt_data():
	data = request.get_json()
	return security.encrypt(data['data'])

@app.route('/decrypt', methods=['POST'])
def decrypt_data():
	data = request.get_json()
	return security.decrypt(data['data'])

@app.route('/switch_theme', methods=['POST'])
def switch_theme():
	data = request.get_json()
	return ui.switch_theme(data['theme'])

@app.route('/adjust_screen_size', methods=['POST'])
def adjust_screen_size():
	data = request.get_json()
	return ui.adjust_screen_size(data['screen_size'])

@app.route('/preview_file', methods=['GET'])
def preview_file():
	data = request.get_json()
	return ui.preview_file(data['file'])

if __name__ == '__main__':
	app.run(debug=True)
