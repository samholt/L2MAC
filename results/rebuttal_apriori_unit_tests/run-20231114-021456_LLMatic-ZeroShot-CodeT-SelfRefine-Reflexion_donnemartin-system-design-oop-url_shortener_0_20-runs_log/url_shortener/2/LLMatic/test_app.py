import pytest
from app import app

def test_app():
	with app.test_client() as c:
		resp = c.get('/')
		assert resp.status_code == 404
