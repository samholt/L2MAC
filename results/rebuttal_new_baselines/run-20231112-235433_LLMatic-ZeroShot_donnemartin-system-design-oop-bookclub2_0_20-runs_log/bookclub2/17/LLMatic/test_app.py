import pytest
import app


def test_create_user():
	response = app.app.test_client().post('/create_user', json={'user_id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200


def test_create_club():
	response = app.app.test_client().post('/create_club', json={'club_name': 'Test Club', 'user_id': '1'})
	assert response.status_code == 200


def test_join_club():
	response = app.app.test_client().post('/join_club', json={'club_name': 'Test Club', 'user_id': '2'})
	assert response.status_code == 200


def test_set_privacy():
	response = app.app.test_client().post('/set_privacy', json={'club_name': 'Test Club', 'privacy': 'private'})
	assert response.status_code == 200


def test_manage_roles():
	response = app.app.test_client().post('/manage_roles', json={'user_id': '1', 'role': 'admin'})
	assert response.status_code == 200
