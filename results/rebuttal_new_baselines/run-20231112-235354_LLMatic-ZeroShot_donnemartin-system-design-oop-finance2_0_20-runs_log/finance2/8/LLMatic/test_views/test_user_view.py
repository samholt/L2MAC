import pytest
from flask import Flask, json
from views.user_view import register, login

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_view():
	return register()

@app.route('/login', methods=['POST'])
def login_view():
	return login()


def test_register():
	with app.test_client() as client:
		response = client.post('/register', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 201
		assert data['message'] == 'User registered successfully'
		assert data['user']['name'] == 'Test User'
		assert data['user']['email'] == 'test@example.com'


def test_login():
	with app.test_client() as client:
		client.post('/register', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
		response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
		data = json.loads(response.get_data(as_text=True))
		assert response.status_code == 200
		assert data['message'] == 'Logged in successfully'
