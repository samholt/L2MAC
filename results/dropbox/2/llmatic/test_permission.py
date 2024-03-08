import pytest
from permission import Permission


def test_check_permission():
	permission = Permission('user1', 'read')
	assert permission.check_permission('user1') == True
	assert permission.check_permission('user2') == False


def test_change_permission():
	permission = Permission('user1', 'read')
	permission.change_permission('user2', 'write')
	assert permission.user == 'user2'
	assert permission.access_type == 'write'
