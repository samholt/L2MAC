import pytest
import app

def test_home():
	client = app.app.test_client()
	response = client.get('/')
	assert response.status_code == 200
