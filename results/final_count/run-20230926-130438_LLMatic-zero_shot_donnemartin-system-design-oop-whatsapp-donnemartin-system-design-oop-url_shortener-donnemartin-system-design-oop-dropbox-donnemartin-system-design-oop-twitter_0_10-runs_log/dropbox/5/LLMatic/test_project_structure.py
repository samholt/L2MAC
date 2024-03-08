import os

def test_project_structure():
	assert os.path.exists('main.py')
	assert os.path.exists('user_management.py')
	assert os.path.exists('file_management.py')
	assert os.path.exists('file_sharing.py')
	assert os.path.exists('security.py')
	assert os.path.exists('requirements.txt')
