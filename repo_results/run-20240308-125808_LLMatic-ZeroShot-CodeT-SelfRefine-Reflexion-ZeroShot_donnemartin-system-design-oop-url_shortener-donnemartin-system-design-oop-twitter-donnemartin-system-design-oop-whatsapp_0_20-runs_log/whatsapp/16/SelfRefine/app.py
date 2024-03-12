from flask import Flask, request, jsonify
from user import User
from chat import Chat
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

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
	return {'message': 'Invalid credentials'}, 401

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	db.session.add(chat)
	db.session.commit()
	return jsonify(chat.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
