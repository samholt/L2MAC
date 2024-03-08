from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, Post
from app import db

user_blueprint = Blueprint('user', __name__)
post_blueprint = Blueprint('post', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	new_user = User(username=data['username'], email=data['email'])
	new_user.set_password(data['password'])
	db.session.add(new_user)
	db.session.commit()
	return jsonify({'message': 'Registered successfully'}), 201


@user_blueprint.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	user = User.query.filter_by(username=data['username']).first()
	if user and user.check_password(data['password']):
		access_token = create_access_token(identity=user.username)
		return jsonify(access_token=access_token), 200
	return jsonify({'message': 'Invalid credentials'}), 401


@post_blueprint.route('/post', methods=['POST'])
@jwt_required

def create_post():
	data = request.get_json()
	user_id = User.query.filter_by(username=get_jwt_identity()).first().id
	new_post = Post(content=data['content'], user_id=user_id)
	db.session.add(new_post)
	db.session.commit()
	return jsonify({'message': 'Post created'}), 201
