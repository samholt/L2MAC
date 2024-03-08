import pytest
import main

def test_home():
	response = main.app.test_client().get('/')
	assert response.status_code == 200
	assert response.data == b'Hello, World!'
