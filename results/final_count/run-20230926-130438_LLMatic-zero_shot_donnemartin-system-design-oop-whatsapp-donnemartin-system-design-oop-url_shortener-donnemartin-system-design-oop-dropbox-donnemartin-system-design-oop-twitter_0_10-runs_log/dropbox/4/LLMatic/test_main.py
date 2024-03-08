import pytest
from main import app

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.data == b'Hello, World!'
