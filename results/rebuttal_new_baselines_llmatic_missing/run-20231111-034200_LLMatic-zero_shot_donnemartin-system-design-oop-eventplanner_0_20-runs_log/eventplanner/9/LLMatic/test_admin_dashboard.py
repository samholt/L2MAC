import pytest
from admin_dashboard import app
from flask import url_for
from werkzeug.wrappers import response

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.app_context():
		with app.test_client() as client:
			yield client


def test_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
	assert b'User Activities' in response.data
	assert b'System Performance' in response.data
	assert b'Vendor Listings' in response.data
