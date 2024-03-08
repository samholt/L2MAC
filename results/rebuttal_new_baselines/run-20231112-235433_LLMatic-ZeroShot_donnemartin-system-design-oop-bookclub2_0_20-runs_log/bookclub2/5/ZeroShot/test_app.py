import pytest
import app
from flask import json


def test_create_user():
	app.users = {}
	response = app.app.test_client().post('/users', data=json.dumps({'id': '1', 'name': 'Alice'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Alice', 'clubs': {}}
	assert '1' in app.users


def test_create_club():
	app.users = {'1': app.User(id='1', name='Alice', clubs={})}
	response = app.app.test_client().post('/clubs', data=json.dumps({'id': '1', 'name': 'Book Club', 'creator': '1'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'id': '1', 'name': 'Book Club', 'creator': '1', 'members': ['1']}
	assert '1' in app.clubs
	assert '1' in app.users['1'].clubs
