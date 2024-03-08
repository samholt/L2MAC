import jwt
import datetime

SECRET_KEY = 'secret'


def generate_token(username):
	payload = {
		'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=5),
		'iat': datetime.datetime.utcnow(),
		'sub': username
	}
	return jwt.encode(
		payload,
		SECRET_KEY,
		algorithm='HS256'
	)

def decode_token(token):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		return 'Signature expired. Please log in again.'
	except jwt.InvalidTokenError:
		return 'Invalid token. Please log in again.'
