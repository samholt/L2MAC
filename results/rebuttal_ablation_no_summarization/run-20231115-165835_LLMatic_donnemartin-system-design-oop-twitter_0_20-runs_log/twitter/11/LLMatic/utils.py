import jwt
import datetime
from models import User, users_db

SECRET_KEY = 'secret'


def validate_user_input(username, email, password):
	if not username or not email or not password:
		return False
	return True


def generate_token(user):
	payload = {
		'user_id': user.username,
		'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
	}
	token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
	return token
