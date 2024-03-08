from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Serializer, SignatureExpired, BadSignature
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

s = Serializer(app.config['SECRET_KEY'])


def hash_password(password):
	return generate_password_hash(password)


def check_password(password_hash, password):
	return check_password_hash(password_hash, password)


def generate_auth_token(user_id, expiration=600):
	return s.dumps({'id': user_id})


def verify_auth_token(token):
	try:
		data = s.loads(token)
	except SignatureExpired:
		return None
	except BadSignature:
		return None
	return data['id']


def mock_payment_gateway(amount):
	if amount > 0:
		return True
	else:
		return False
