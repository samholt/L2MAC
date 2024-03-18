from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
from chat import Chat

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	user = User(data['email'], hashed_password)
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(email=data['email']).first()
	if user and check_password_hash(user.password, data['password']):
		return jsonify(user.to_dict()), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/users/<user_id>/chats', methods=['POST'])
def create_chat(user_id):
	data = request.get_json()
	chat = Chat(data['name'])
	chat.users.append(User.query.get(user_id))
	db.session.add(chat)
	db.session.commit()
	return jsonify(chat.to_dict()), 201

@app.route('/users/<user_id>/chats/<chat_id>/messages', methods=['POST'])
def send_message(user_id, chat_id):
	data = request.get_json()
	message = chats[chat_id].send_message(users[user_id], data['content'])
	db.session.add(message)
	db.session.commit()
	return jsonify(message.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
