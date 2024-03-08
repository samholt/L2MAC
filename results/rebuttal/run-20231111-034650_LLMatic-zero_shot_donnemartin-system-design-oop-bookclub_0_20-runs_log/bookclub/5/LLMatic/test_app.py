import pytest
from app import app
from models import User, Book, Admin, Notification, Resource

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

# Existing tests...

def test_view_resources(client):
	response = client.get('/view_resources')
	assert response.status_code == 200

	# Add a resource to the mock database
	resource = Resource('Test Resource', 'This is a test resource', 'Test Author')
	app.resources[resource.title] = resource

	response = client.get('/view_resources')
	assert response.status_code == 200
	assert len(response.get_json()['resources']) == 1

def test_contribute_resource(client):
	response = client.post('/contribute_resource', json={'title': 'New Resource', 'content': 'This is a new resource', 'author': 'New Author'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Resource contributed successfully'
	assert 'New Resource' in app.resources
