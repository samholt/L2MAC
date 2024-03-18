import pytest
import app
import url_shortener
import user_accounts
import analytics

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_admin_dashboard(client):
	response = client.get('/admin/dashboard')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert 'users' in response.get_json()


def test_delete_url(client):
	url_shortener.url_database['test'] = 'http://test.com'
	response = client.delete('/admin/delete_url/test')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL deleted successfully'


def test_delete_user(client):
	app.user_accounts.register('test', 'test')
	response = client.delete('/admin/delete_user/test')
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'User deleted successfully'


def test_analytics_dashboard(client):
	response = client.get('/admin/analytics')
	assert response.status_code == 200
	assert 'total_urls' in response.get_json()
	assert 'total_clicks' in response.get_json()
