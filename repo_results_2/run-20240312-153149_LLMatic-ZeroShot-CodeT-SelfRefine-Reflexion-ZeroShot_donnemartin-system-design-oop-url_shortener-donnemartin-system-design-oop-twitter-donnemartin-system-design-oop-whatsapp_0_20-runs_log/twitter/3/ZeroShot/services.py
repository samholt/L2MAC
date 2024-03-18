from models import User
from app import db


def register_user(data):
	user = User(username=data['username'], email=data['email'], password=data['password'])
	db.session.add(user)
	db.session.commit()
	return user


def authenticate_user(data):
	user = User.query.filter_by(username=data['username']).first()
	if user and user.password == data['password']:
		return user
	return None


def get_user(username):
	user = User.query.filter_by(username=username).first()
	if user:
		return user
	return None


def update_user(username, data):
	user = User.query.filter_by(username=username).first()
	if user:
		user.bio = data.get('bio', user.bio)
		user.website = data.get('website', user.website)
		user.location = data.get('location', user.location)
		user.is_private = data.get('is_private', user.is_private)
		db.session.commit()
		return user
	return None
