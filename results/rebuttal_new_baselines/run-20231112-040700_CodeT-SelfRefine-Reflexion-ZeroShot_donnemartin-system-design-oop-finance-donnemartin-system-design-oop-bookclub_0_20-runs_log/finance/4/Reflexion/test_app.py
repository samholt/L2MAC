import pytest
import requests
from multiprocessing import Process
from app import app

@pytest.fixture(scope='module')
def test_server():
	# Start the Flask app in a separate process
	server = Process(target=app.run)
	server.start()
	yield server
	# Stop the Flask app after tests are done
	server.terminate()

@pytest.mark.usefixtures('test_server')
def test_create_user():
	response = requests.post('http://localhost:5000/create_user', json={'id': '1', 'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.json() == {'id': '1', 'username': 'test', 'password': 'test'}

@pytest.mark.usefixtures('test_server')
def test_add_transaction():
	response = requests.post('http://localhost:5000/add_transaction', json={'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'})
	assert response.status_code == 201
	assert response.json() == {'id': '1', 'user_id': '1', 'amount': 100.0, 'category': 'groceries'}
