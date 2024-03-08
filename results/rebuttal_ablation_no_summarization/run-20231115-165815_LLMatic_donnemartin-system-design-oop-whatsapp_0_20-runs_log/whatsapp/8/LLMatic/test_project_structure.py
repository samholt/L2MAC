import os

def test_project_structure():
	assert os.path.exists('auth.py')
	assert os.path.exists('profile.py')
	assert os.path.exists('contacts.py')
	assert os.path.exists('messaging.py')
	assert os.path.exists('groups.py')
	assert os.path.exists('status.py')
	assert os.path.exists('webapp.py')
	assert os.path.exists('connectivity.py')
	assert os.path.exists('main.py')
	assert os.path.exists('requirements.txt')
