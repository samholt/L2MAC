import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('user.py')
	assert os.path.exists('file.py')
	assert os.path.exists('share.py')
	assert os.path.exists('security.py')
	assert os.path.exists('ui.py')
	assert os.path.exists('requirements.txt')
