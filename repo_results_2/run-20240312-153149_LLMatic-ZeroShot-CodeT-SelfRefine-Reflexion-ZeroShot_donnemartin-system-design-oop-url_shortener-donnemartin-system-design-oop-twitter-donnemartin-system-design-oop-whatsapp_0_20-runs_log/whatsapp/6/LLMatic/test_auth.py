import json
import app

def test_signup():
	app.app.testing = True
	client = app.app.test_client()

	# Test signup with missing parameters
	response = client.post('/signup', data=json.dumps({}), content_type='application/json')
	assert response.status_code == 400

	# Test successful signup
	response = client.post('/signup', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert app.DATABASE['users']['test@example.com'] == {'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': '', 'blocked': [], 'online': False}

def test_login():
	app.app.testing = True
	client = app.app.test_client()

	# Test login with missing parameters
	response = client.post('/login', data=json.dumps({}), content_type='application/json')
	assert response.status_code == 401

	# Test login with invalid credentials
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'wrong_password'}), content_type='application/json')
	assert response.status_code == 401

	# Test successful login
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE['users']['test@example.com']['online'] == True

def test_logout():
	app.app.testing = True
	client = app.app.test_client()

	# Test logout with missing parameters
	response = client.post('/logout', data=json.dumps({}), content_type='application/json')
	assert response.status_code == 400

	# Test successful logout
	response = client.post('/logout', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert app.DATABASE['users']['test@example.com']['online'] == False
