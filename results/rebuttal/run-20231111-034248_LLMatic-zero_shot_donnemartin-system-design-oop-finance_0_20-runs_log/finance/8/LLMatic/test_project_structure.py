import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('config.py')
	assert os.path.exists('models.py')
	assert os.path.exists('auth.py')
	assert os.path.exists('data.py')
	assert os.path.exists('requirements.txt')
