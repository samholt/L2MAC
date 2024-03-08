from models import User, Post, Follow
from app import db, jwt
from flask_jwt_extended import create_access_token

@jwt.user_identity_loader
def user_identity_lookup(user):
	return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
	identity = jwt_data['identity']
	return User.query.filter_by(id=identity).one_or_none()

def register_user(data):
	user = User(id=data['id'], username=data['username'], email=data['email'], password=data['password'])
	db.session.add(user)
	db.session.commit()

def authenticate_user(data):
	user = User.query.filter_by(username=data['username']).first()
	if user and user.password == data['password']:
		access_token = create_access_token(identity=user)
		return access_token
	else:
		return None

def create_post(data):
	post = Post(id=data['id'], user_id=data['user_id'], content=data['content'])
	db.session.add(post)
	db.session.commit()

def follow_user(data):
	follow = Follow(follower_id=data['follower_id'], followed_id=data['followed_id'])
	db.session.add(follow)
	db.session.commit()

def unfollow_user(data):
	follow = Follow.query.filter_by(follower_id=data['follower_id'], followed_id=data['followed_id']).first()
	if follow:
		db.session.delete(follow)
		db.session.commit()
