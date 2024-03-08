from flask import Flask, request, jsonify
import views
from models import User

app = Flask(__name__)

db = {}

@app.route('/')
def home():
	return 'URL Shortening Service'

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username')
	password = data.get('password')

	if username in db:
		return jsonify({'error': 'User already exists'}), 400

	db[username] = User(username, password)
	return jsonify({'message': 'User created successfully'}), 200

app.register_blueprint(views.app)

if __name__ == '__main__':
	app.run(debug=True)
