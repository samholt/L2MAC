import app
import admin_dashboard
import json

def test_admin_delete_url():
	with app.app.test_client() as c:
		admin_dashboard.url_db['google'] = 'abc123'
		response = c.post('/admin/delete_url', data={'url': 'google'})
		assert response.status_code == 200
		assert json.loads(response.data) == {'message': 'URL deleted successfully'}


def test_admin_delete_user():
	with app.app.test_client() as c:
		admin_dashboard.user_db['test'] = {'password': 'password', 'urls': []}
		response = c.post('/admin/delete_user', data={'username': 'test'})
		assert response.status_code == 200
		assert json.loads(response.data) == {'message': 'User deleted successfully'}


def test_admin_monitor_system():
	with app.app.test_client() as c:
		admin_dashboard.url_db = {'http://example.com': 'abc123'}
		admin_dashboard.user_db = {'testuser': {'password': 'password', 'urls': []}}
		response = c.get('/admin/monitor_system')
		assert response.status_code == 200
		assert json.loads(response.data) == {'total_urls': 1, 'total_users': 1}
