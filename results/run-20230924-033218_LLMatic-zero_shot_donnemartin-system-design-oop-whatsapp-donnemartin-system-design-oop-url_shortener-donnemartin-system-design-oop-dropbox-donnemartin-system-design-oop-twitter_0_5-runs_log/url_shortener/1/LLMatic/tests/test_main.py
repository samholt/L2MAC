import pytest
from main import app

def test_home():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 200
		assert resp.data == b'Welcome to the URL Shortener Service!'
