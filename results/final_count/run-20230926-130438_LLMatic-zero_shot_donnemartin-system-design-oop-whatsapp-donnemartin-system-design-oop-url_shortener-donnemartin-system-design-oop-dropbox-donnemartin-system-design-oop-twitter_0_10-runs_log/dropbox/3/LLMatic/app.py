from flask import Flask, request
from user import register, login, forgot_password, profile, change_password
from file import File, Folder, FileDatabase
from share import Share
from security import encrypt_file, decrypt_file, log_activity
from ui import UI

app = Flask(__name__)
file_db = FileDatabase()
share = Share()

@app.route('/register', methods=['POST'])
def register_user():
	data = request.get_json()
	user = register(data['name'], data['email'], data['password'])
	return {'status': 'success', 'message': 'User registered successfully', 'user': user.__dict__}, 200

@app.route('/login', methods=['POST'])
def login_user():
	data = request.get_json()
	if login(data['email'], data['password']):
		return {'status': 'success', 'message': 'User logged in successfully'}, 200
	return {'status': 'error', 'message': 'Invalid email or password'}, 400

@app.route('/forgot_password', methods=['POST'])
def reset_password():
	data = request.get_json()
	if forgot_password(data['email'], data['new_password']):
		return {'status': 'success', 'message': 'Password reset successfully'}, 200
	return {'status': 'error', 'message': 'Invalid email'}, 400

@app.route('/profile', methods=['GET'])
def get_profile():
	data = request.args
	user_profile = profile(data['email'])
	if user_profile:
		return {'status': 'success', 'profile': user_profile}, 200
	return {'status': 'error', 'message': 'Invalid email'}, 400

@app.route('/change_password', methods=['POST'])
def update_password():
	data = request.get_json()
	if change_password(data['email'], data['new_password']):
		return {'status': 'success', 'message': 'Password changed successfully'}, 200
	return {'status': 'error', 'message': 'Invalid email'}, 400

@app.route('/upload', methods=['POST'])
def upload_file():
	data = request.get_json()
	file = File(data['name'], data['type'], data['size'], data['content'])
	file_db.upload(file, data.get('folder_name'))
	return {'status': 'success', 'message': 'File uploaded successfully'}, 200

@app.route('/download', methods=['GET'])
def download_file():
	data = request.args
	file = file_db.download(data['file_name'], data.get('folder_name'))
	if file:
		return {'status': 'success', 'file': file.__dict__}, 200
	return {'status': 'error', 'message': 'File not found'}, 400

@app.route('/create_folder', methods=['POST'])
def create_folder():
	data = request.get_json()
	folder = Folder(data['name'])
	file_db.create_folder(folder)
	return {'status': 'success', 'message': 'Folder created successfully'}, 200

@app.route('/move_file', methods=['POST'])
def move_file():
	data = request.get_json()
	file_db.move_file(data['file_name'], data['folder_name'])
	return {'status': 'success', 'message': 'File moved successfully'}, 200

@app.route('/share_file', methods=['POST'])
def share_file():
	data = request.get_json()
	share.share_file(data['file_name'], data['email'])
	return {'status': 'success', 'message': 'File shared successfully'}, 200

@app.route('/encrypt_file', methods=['POST'])
def encrypt_file_route():
	data = request.get_json()
	encrypt_file(data['file_name'])
	return {'status': 'success', 'message': 'File encrypted successfully'}, 200

@app.route('/log_activity', methods=['POST'])
def log_activity_route():
	data = request.get_json()
	log_activity(data['user_email'], data['activity'])
	return {'status': 'success', 'message': 'Activity logged successfully'}, 200

if __name__ == '__main__':
	app.run(debug=True)
