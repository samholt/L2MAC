import app
import json
from flask import Flask, request
from werkzeug.wrappers import Response

app.app.testing = True
client = app.app.test_client()

def test_database():
	# Test that the database is initially empty
	for key in app.DATABASE:
		assert len(app.DATABASE[key]) == 0

	# Test adding data to the database
	app.DATABASE['users']['test_user'] = 'test_data'
	assert app.DATABASE['users']['test_user'] == 'test_data'

	# Test removing data from the database
	del app.DATABASE['users']['test_user']
	assert 'test_user' not in app.DATABASE['users']

def test_user_registration():
	# Test user registration
	new_user = app.User('test_user', 'test_password', 'test_email')
	app.DATABASE['users'][new_user.username] = new_user
	assert app.DATABASE['users']['test_user'] == new_user

	# Test user login
	response = client.post('/login', data=json.dumps({'username': 'test_user', 'password': 'test_password'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Login successful'
	response = client.post('/login', data=json.dumps({'username': 'test_user', 'password': 'wrong_password'}), content_type='application/json')
	assert response.status_code == 401
	assert json.loads(response.data)['message'] == 'Invalid username or password'

def test_book_club_creation():
	# Test book club creation
	new_book_club = app.BookClub('test_book_club', 'public', ['test_user'], 'test_book')
	app.DATABASE['book_clubs'][new_book_club.name] = new_book_club
	assert app.DATABASE['book_clubs']['test_book_club'] == new_book_club

	# Test joining book club
	response = client.post('/join_book_club', data=json.dumps({'username': 'test_user', 'book_club_name': 'test_book_club'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Joined book club successfully'
	response = client.post('/join_book_club', data=json.dumps({'username': 'test_user', 'book_club_name': 'non_existent_book_club'}), content_type='application/json')
	assert response.status_code == 401
	assert json.loads(response.data)['message'] == 'Book club not found or is private'
