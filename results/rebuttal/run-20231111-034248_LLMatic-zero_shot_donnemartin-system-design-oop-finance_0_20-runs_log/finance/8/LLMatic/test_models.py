import pytest
from models import User


def test_add_notification():
	user = User.create_user('test_user', 'test_password', 'test_email')
	user.add_notification('Test notification')
	assert 'Test notification' in user.notifications


def test_remove_notification():
	user = User.create_user('test_user', 'test_password', 'test_email')
	user.add_notification('Test notification')
	user.remove_notification('Test notification')
	assert 'Test notification' not in user.notifications


def test_add_alert():
	user = User.create_user('test_user', 'test_password', 'test_email')
	user.add_alert('Test alert')
	assert 'Test alert' in user.alerts


def test_remove_alert():
	user = User.create_user('test_user', 'test_password', 'test_email')
	user.add_alert('Test alert')
	user.remove_alert('Test alert')
	assert 'Test alert' not in user.alerts


def test_check_for_unusual_activity():
	user = User.create_user('test_user', 'test_password', 'test_email')
	unusual_transactions = user.check_for_unusual_activity()
	assert unusual_transactions
	assert 'Unusual activity detected in your account.' in user.alerts
