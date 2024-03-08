import pytest
import requests
from multiprocessing import Process
from app import app as flask_app
import time

@pytest.fixture(scope='session')
def client():
	server = Process(target=flask_app.run, kwargs={'port': 5002})
	server.start()
	time.sleep(1)  # Wait for the server to start
	yield requests.Session()
	server.terminate()
	server.join()

def test_create_user(client):
	response = client.post('http://localhost:5002/api/users', json={'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.json() == {'message': 'User created'}

def test_update_status(client):
	response = client.post('http://localhost:5002/api/update_status', json={'email': 'test@test.com', 'status': 'Hello, world!'})
	assert response.status_code == 200
	assert response.json() == {'message': 'Status updated'}

def test_add_contact(client):
	response = client.post('http://localhost:5002/api/add_contact', json={'email': 'test@test.com', 'contact_email': 'test1@test.com'})
	assert response.status_code == 200
	assert response.json() == {'message': 'Contact added'}

def test_send_message(client):
	response = client.post('http://localhost:5002/api/send_message', json={'from_email': 'test@test.com', 'to_email': 'test1@test.com', 'message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.json() == {'message': 'Message sent'}

def test_create_group(client):
	response = client.post('http://localhost:5002/api/create_group', json={'group_name': 'Test Group', 'emails': ['test@test.com', 'test1@test.com']})
	assert response.status_code == 201
	assert response.json() == {'message': 'Group created'}

def test_update_status_visibility(client):
	response = client.post('http://localhost:5002/api/update_status_visibility', json={'email': 'test@test.com', 'status_visibility': ['test1@test.com']})
	assert response.status_code == 200
	assert response.json() == {'message': 'Status visibility updated'}
