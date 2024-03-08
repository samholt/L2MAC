import pytest
import security
from database import Database


def test_add_security_detail():
	security.db = Database()
	response = security.app.test_client().post('/add_security_detail', json={'user_id': '1', 'security_detail': 'encrypted_data'})
	assert response.status_code == 200
	assert response.get_json() == {'status': 'success'}


def test_get_security_detail():
	security.db = Database()
	security.db.add_security_detail('1', 'encrypted_data')
	response = security.app.test_client().get('/get_security_detail?user_id=1')
	assert response.status_code == 200
	assert response.get_json() == {'status': 'success', 'data': 'encrypted_data'}


def test_get_security_detail_not_found():
	security.db = Database()
	response = security.app.test_client().get('/get_security_detail?user_id=1')
	assert response.status_code == 404
	assert response.get_json() == {'status': 'failure', 'message': 'No security detail found for this user'}
