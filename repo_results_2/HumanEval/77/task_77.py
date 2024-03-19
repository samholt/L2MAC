def iscube(a):
	''' 
	This function takes an integer a and returns True if this integer is a cube of some integer number.
	Note: you may assume the input is always valid.
	Examples:
	iscube(1) ==> True
	iscube(2) ==> False
	iscube(-1) ==> True
	iscube(64) ==> True
	iscube(0) ==> True
	iscube(180) ==> False
	'''
	if a < 0:
		return iscube(-a)
	else:
		return round(a ** (1/3)) ** 3 == a


import pytest

def test_iscube():
	assert iscube(1) == True
	assert iscube(2) == False
	assert iscube(-1) == True
	assert iscube(64) == True
	assert iscube(0) == True
	assert iscube(180) == False
	assert iscube(27) == True
	assert iscube(-27) == True
	assert iscube(100) == False
	assert iscube(-100) == False

pytest.main()
