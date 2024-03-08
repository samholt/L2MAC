import pytest
import requests
import json
from multiprocessing import Process
from app import app
from time import sleep

base_url = 'http://localhost:5001'

@pytest.fixture(scope='session', autouse=True)
def server():
	def run_server():
		app.run(port=5001, use_reloader=False)
	server = Process(target=run_server)
	server.start()
	sleep(1)  # Ensure the server has time to start
	yield server
	server.terminate()

@pytest.fixture
def user():
	return {'username': 'testuser', 'password': 'testpass', 'email': 'testuser@test.com'}

@pytest.fixture
def book_club():
	return {'name': 'testclub', 'privacy_settings': 'public', 'members': [], 'administrators': ['testuser']}

@pytest.fixture
def meeting():
	return {'date': '2022-01-01', 'time': '10:00', 'attendees': ['testuser'], 'reminders': []}

@pytest.fixture
def discussion():
	return {'topic': 'testtopic'}

@pytest.fixture
def admin():
	return {}


def test_create_user(user):
	response = requests.post(f'{base_url}/user', json=user)
	assert response.status_code == 201
	assert response.json()['message'] == 'User created'


def test_get_user(user):
	requests.post(f'{base_url}/user', json=user)
	response = requests.get(f'{base_url}/user/{user["username"]}')
	assert response.status_code == 200
	assert response.json()['username'] == user['username']


def test_create_book_club(book_club):
	response = requests.post(f'{base_url}/book_club', json=book_club)
	assert response.status_code == 201
	assert response.json()['message'] == 'Book club created'


def test_get_book_club(book_club):
	requests.post(f'{base_url}/book_club', json=book_club)
	response = requests.get(f'{base_url}/book_club/{book_club["name"]}')
	assert response.status_code == 200
	assert response.json()['name'] == book_club['name']


def test_create_meeting(meeting):
	response = requests.post(f'{base_url}/meeting', json=meeting)
	assert response.status_code == 201
	assert response.json()['message'] == 'Meeting scheduled'


def test_get_meeting(meeting):
	requests.post(f'{base_url}/meeting', json=meeting)
	response = requests.get(f'{base_url}/meeting/{meeting["date"]}')
	assert response.status_code == 200
	assert response.json()['date'] == meeting['date']


def test_create_discussion(discussion):
	response = requests.post(f'{base_url}/discussion', json=discussion)
	assert response.status_code == 201
	assert response.json()['message'] == 'Discussion created'


def test_get_discussion(discussion):
	requests.post(f'{base_url}/discussion', json=discussion)
	response = requests.get(f'{base_url}/discussion/{discussion["topic"]}')
	assert response.status_code == 200
	assert response.json()['topic'] == discussion['topic']


def test_create_admin(admin):
	response = requests.post(f'{base_url}/admin', json=admin)
	assert response.status_code == 201
	assert response.json()['message'] == 'Admin created'
