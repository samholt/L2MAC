from flask import Flask, request
from user_management import User, register, login, forgot_password, get_profile, change_password
from file_management import File, Folder, upload_file, download_file
from file_sharing import generate_link, invite_user
from utils import log_activity, encrypt, decrypt

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
	user = User(**request.json)
	message = register(user)
	return {'message': message}

@app.route('/login', methods=['POST'])
def login_user():
	email = request.json.get('email')
	password = request.json.get('password')
	message = login(email, password)
	return {'message': message}

@app.route('/forgot_password', methods=['POST'])
def reset_password():
	email = request.json.get('email')
	message = forgot_password(email)
	return {'message': message}

@app.route('/profile', methods=['GET'])
def view_profile():
	user = User(**request.json)
	profile = get_profile(user)
	return {'profile': profile}

@app.route('/change_password', methods=['POST'])
def update_password():
	user = User(**request.json.get('user'))
	new_password = request.json.get('new_password')
	message = change_password(user, new_password)
	return {'message': message}

@app.route('/upload_file', methods=['POST'])
def upload():
	file = File(**request.json)
	message = upload_file(file)
	return {'message': message}

@app.route('/download_file', methods=['GET'])
def download():
	file_name = request.json.get('file_name')
	file = download_file(file_name)
	return {'file': file}

@app.route('/generate_link', methods=['POST'])
def generate():
	file_or_folder = request.json.get('file_or_folder')
	link = generate_link(file_or_folder)
	return {'link': link}

@app.route('/invite_user', methods=['POST'])
def invite():
	folder = Folder(**request.json.get('folder'))
	user = request.json.get('user')
	invite_user(folder, user)
	return {'message': 'User invited'}

if __name__ == '__main__':
	app.run(debug=True)
