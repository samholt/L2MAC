from flask import request, jsonify
from app import app, db
from models import User, Post
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


@app.route('/register', methods=['POST'])
def register():
	username = request.json.get('username', None)
	email = request.json.get('email', None)
	password = request.json.get('password', None)

	if not username:
		return jsonify({'msg': 'Missing username parameter'}), 400
	if not email:
		return jsonify({'msg': 'Missing email parameter'}), 400
	if not password:
		return jsonify({'msg': 'Missing password parameter'}), 400

	user = User(username=username, email=email, password=password)
	db.session.add(user)
	db.session.commit()

	return jsonify({'msg': 'User created'}), 201


@app.route('/login', methods=['POST'])
def login():
	username = request.json.get('username', None)
	password = request.json.get('password', None)

	user = User.query.filter_by(username=username, password=password).first()

	if user is None:
		return jsonify({'msg': 'Bad username or password'}), 401

	access_token = create_access_token(identity=username)
	return jsonify(access_token=access_token), 200


@app.route('/post', methods=['POST'])
@jwt_required

def post():
	content = request.json.get('content', None)

	if not content:
		return jsonify({'msg': 'Missing content parameter'}), 400

	username = get_jwt_identity()
	user = User.query.filter_by(username=username).first()

	post = Post(content=content, user_id=user.id)
	db.session.add(post)
	db.session.commit()

	return jsonify({'msg': 'Post created'}), 201
