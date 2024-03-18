import pytest
from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views)

def test_register():
	with app.test_client() as c:
		response = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'User registered successfully'}

		response = c.post('/register', json={'email': 'test@test.com', 'username': 'test', 'password': 'test'})
		assert response.status_code == 400
		assert response.get_json() == {'message': 'User already exists'}

def test_login():
	with app.test_client() as c:
		response = c.post('/login', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 200
		assert 'token' in response.get_json()

		response = c.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid credentials'}

def test_password_reset():
	with app.test_client() as c:
		response = c.post('/password_reset_request', json={'email': 'nonexistent@test.com'})
		assert response.status_code == 404
		assert response.get_json() == {'message': 'User not found'}

		response = c.post('/password_reset_request', json={'email': 'test@test.com'})
		assert response.status_code == 200
		assert 'password_reset_link' in response.get_json()

		password_reset_link = response.get_json()['password_reset_link']
		email, token = password_reset_link[:-43], password_reset_link[-43:]

		response = c.post('/password_reset', json={'email': email, 'token': 'wrong', 'new_password': 'newtest'})
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid password reset link'}

		response = c.post('/password_reset', json={'email': email, 'token': token, 'new_password': 'newtest'})
		assert response.status_code == 200
		assert response.get_json() == {'message': 'Password reset successfully'}

		response = c.post('/login', json={'email': 'test@test.com', 'password': 'newtest'})
		assert response.status_code == 200
		assert 'token' in response.get_json()

		response = c.post('/login', json={'email': 'test@test.com', 'password': 'test'})
		assert response.status_code == 400
		assert response.get_json() == {'message': 'Invalid credentials'}
