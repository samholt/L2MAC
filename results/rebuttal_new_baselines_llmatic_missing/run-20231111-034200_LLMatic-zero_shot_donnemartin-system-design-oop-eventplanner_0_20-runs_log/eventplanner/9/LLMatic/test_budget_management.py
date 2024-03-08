import pytest
import budget_management


def test_set_budget():
	with budget_management.app.test_client() as c:
		response = c.post('/budget', json={'total': 1000, 'spent': 0})
		assert response.status_code == 201
		assert 'id' in response.get_json()


def test_get_budget():
	with budget_management.app.test_client() as c:
		response = c.post('/budget', json={'total': 1000, 'spent': 0})
		id = response.get_json()['id']
		response = c.get(f'/budget/{id}')
		assert response.status_code == 200
		assert response.get_json()['total'] == 1000
		assert response.get_json()['spent'] == 0


def test_update_budget():
	with budget_management.app.test_client() as c:
		response = c.post('/budget', json={'total': 1000, 'spent': 0})
		id = response.get_json()['id']
		response = c.put(f'/budget/{id}', json={'spent': 500})
		assert response.status_code == 200
		assert response.get_json()['total'] == 1000
		assert response.get_json()['spent'] == 500


def test_check_budget_overrun():
	with budget_management.app.test_client() as c:
		response = c.post('/budget', json={'total': 1000, 'spent': 0})
		id = response.get_json()['id']
		response = c.get(f'/budget/{id}/overrun')
		assert response.status_code == 200
		assert response.get_json()['overrun'] == False
		response = c.put(f'/budget/{id}', json={'spent': 1500})
		response = c.get(f'/budget/{id}/overrun')
		assert response.status_code == 200
		assert response.get_json()['overrun'] == True
