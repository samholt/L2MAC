from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from user import User
from chat import Chat

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(data['email'], data['password'])
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and user.check_password(data['password']):
		return jsonify(user.to_dict()), 200
	return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/users/<user_id>/chats', methods=['POST'])
def create_chat(user_id):
	data = request.get_json()
	chat = Chat(data['name'])
	chat.add_user(user_id)
	db.session.add(chat)
	db.session.commit()
	return jsonify(chat.to_dict()), 201

@app.route('/users/<user_id>/chats/<chat_id>/messages', methods=['POST'])
def send_message(user_id, chat_id):
	data = request.get_json()
	chat = Chat.query.get(chat_id)
	message = chat.send_message(user_id, data['content'])
	db.session.add(message)
	db.session.commit()
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
