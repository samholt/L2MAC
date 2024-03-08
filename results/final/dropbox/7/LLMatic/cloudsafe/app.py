from flask import Flask, render_template
from cloudsafe.controllers import user_controller, file_controller, share_controller, log_controller

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/register', methods=['GET', 'POST'])
def register():
	return user_controller.register()

@app.route('/login', methods=['GET', 'POST'])
def login():
	return user_controller.login()

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	return user_controller.profile()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	return file_controller.upload()

@app.route('/download', methods=['GET', 'POST'])
def download():
	return file_controller.download()

@app.route('/organize', methods=['GET', 'POST'])
def organize():
	return file_controller.organize()

@app.route('/version', methods=['GET', 'POST'])
def version():
	return file_controller.version()

@app.route('/share', methods=['GET', 'POST'])
def share():
	return share_controller.share()

@app.route('/invite', methods=['GET', 'POST'])
def invite():
	return share_controller.invite()

@app.route('/log', methods=['GET', 'POST'])
def log():
	return log_controller.log()

if __name__ == '__main__':
	app.run(debug=True)
