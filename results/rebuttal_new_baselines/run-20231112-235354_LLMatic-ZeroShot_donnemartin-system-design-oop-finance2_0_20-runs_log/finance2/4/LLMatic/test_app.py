import pytest
from app import app

def test_home():
	with app.test_client() as c:
		response = c.get('/')
		assert response.data == b'Hello, World!'
