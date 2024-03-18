import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('config.py')
	assert os.path.exists('user.py')
	assert os.path.exists('post.py')
	assert os.path.exists('auth.py')
	assert os.path.exists('requirements.txt')
