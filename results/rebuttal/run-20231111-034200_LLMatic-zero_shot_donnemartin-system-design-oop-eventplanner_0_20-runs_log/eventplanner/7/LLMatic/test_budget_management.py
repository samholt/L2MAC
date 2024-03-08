import pytest
import json

url = 'http://localhost:5003'

budget = {}


def test_set_budget():
	global budget
	budget = {'limit': 1000, 'current': 500}
	assert budget == {'limit': 1000, 'current': 500}


def test_track_budget():
	global budget
	assert budget['limit'] == 1000
	assert budget['current'] == 500


def test_budget_alert():
	global budget
	if budget['current'] > budget['limit']:
		assert {'alert': 'Budget limit exceeded'}
	else:
		assert {'alert': 'Budget is under control'}
