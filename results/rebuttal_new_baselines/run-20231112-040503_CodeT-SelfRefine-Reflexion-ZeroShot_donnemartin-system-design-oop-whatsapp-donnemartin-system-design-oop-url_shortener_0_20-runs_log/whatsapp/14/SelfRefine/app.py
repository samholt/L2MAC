from flask import Flask, request, jsonify
from database import db
from user import User
from chat import Chat

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

with app.app_context():
	users = db.session.query(User).all()
	chats = db.session.query(Chat).all()

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
	user = db.session.query(User).filter_by(email=data['email'], password=data['password']).first()
	if user:
		return jsonify(user.to_dict()), 200
	return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/chat', methods=['POST'])
def create_chat():
	data = request.get_json()
	chat = Chat(data['name'])
	db.session.add(chat)
	db.session.commit()
	return jsonify(chat.to_dict()), 201

if __name__ == '__main__':
	app.run(debug=True)
