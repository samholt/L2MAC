from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.route('/messaging')
def messaging():
	return render_template('messaging.html')

@app.route('/group_chat')
def group_chat():
	return render_template('group_chat.html')

@app.route('/status')
def status():
	return render_template('status.html')

@app.route('/status/<user_id>')
def user_status(user_id):
	# Mocking user online status
	user_online_status = {'user1': 'online', 'user2': 'offline'}
	return {'user_id': user_id, 'status': user_online_status.get(user_id, 'offline')}

if __name__ == '__main__':
	app.run(debug=True)
