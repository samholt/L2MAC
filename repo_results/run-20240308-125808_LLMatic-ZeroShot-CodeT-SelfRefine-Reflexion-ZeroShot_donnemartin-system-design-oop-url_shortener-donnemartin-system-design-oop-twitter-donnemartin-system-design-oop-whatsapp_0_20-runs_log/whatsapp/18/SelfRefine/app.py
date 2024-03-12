from flask import Flask, request, jsonify
from user import User
from chat import Chat
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
db = SQLAlchemy(app)
jwt = JWTManager(app)

users = {}
chats = {}

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	hashed_password = generate_password_hash(data['password'], method='sha256')
	user = User(data['email'], hashed_password)
	users[user.id] = user
	db.session.add(user)
	db.session.commit()
	return jsonify(user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	for user in users.values():
		if user.email == data['email'] and check_password_hash(user.password, data['password']):
			access_token = create_access_token(identity=user.id)
			return jsonify(access_token=access_token), 200
	return {'message': 'Invalid credentials'}, 401

@app.route('/chat', methods=['POST'])
@jwt_required

def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	chats[chat.id] = chat
	db.session.add(chat)
	db.session.commit()
	return jsonify(chat.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
