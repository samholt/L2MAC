import pytest
from file_sharing.routes import file_sharing, share_links
from flask import Flask, json

app = Flask(__name__)
app.register_blueprint(file_sharing)

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_share(client):
	response = client.post('/share', data=json.dumps({'file_id': '123'}), content_type='application/json')
	assert response.status_code == 200
	assert 'link_id' in response.get_json()
	link_id = response.get_json()['link_id']
	assert link_id in share_links


def test_invite(client):
	response = client.post('/invite', data=json.dumps({'email': 'test@example.com', 'folder_id': '123', 'permissions': 'read'}), content_type='application/json')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'Invitation sent'
