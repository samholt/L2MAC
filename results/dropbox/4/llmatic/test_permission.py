import pytest
from permission import Permission


def test_permission():
	permission = Permission(True, True, True)
	assert permission.read == True
	assert permission.write == True
	assert permission.share == True

	assert permission.check_permission('read') == True
	assert permission.check_permission('write') == True
	assert permission.check_permission('share') == True

	permission.set_permission('read', False)
	assert permission.check_permission('read') == False
