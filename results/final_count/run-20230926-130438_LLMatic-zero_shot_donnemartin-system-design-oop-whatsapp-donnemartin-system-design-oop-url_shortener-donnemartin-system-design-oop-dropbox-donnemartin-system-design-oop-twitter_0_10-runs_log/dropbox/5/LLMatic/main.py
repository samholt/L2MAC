from flask import Flask, render_template, request, redirect, url_for
from user_management import register_user, authenticate_user
from file_management import upload_file, download_file, File
from file_sharing import generate_shareable_link
from security import encrypt_file_content, decrypt_file_content, add_log_entry, Log, generate_key

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
	return 'Home'

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		register_user(name, email, password)
		return redirect(url_for('home'))
	return 'Register'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		if authenticate_user(email, password):
			return redirect(url_for('home'))
		else:
			return 'Invalid credentials'
	return 'Login'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		upload_file(File(file.filename, file.content_type, file.content_length, file.read()))
		return redirect(url_for('home'))
	return 'Upload'

@app.route('/download/<filename>')
def download(filename):
	file = download_file(filename)
	if file:
		return file
	else:
		return 'File not found', 404

@app.route('/share', methods=['GET', 'POST'])
def share():
	if request.method == 'POST':
		filename = request.form['filename']
		generate_shareable_link(filename)
		return redirect(url_for('home'))
	return 'Share'

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
	if request.method == 'POST':
		filename = request.form['filename']
		file = download_file(filename)
		if file:
			key = generate_key()
			encrypted_content = encrypt_file_content(key, file.content)
			file.content = encrypted_content
			upload_file(file)
			return redirect(url_for('home'))
	return 'Encrypt'

@app.route('/log')
def log():
	logs = add_log_entry('log', 'viewed logs')
	return str(logs)

if __name__ == '__main__':
	app.run(debug=True)
