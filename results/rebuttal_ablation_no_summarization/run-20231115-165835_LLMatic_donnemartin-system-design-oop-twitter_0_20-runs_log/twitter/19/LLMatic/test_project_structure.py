import os

def test_project_structure():
	assert os.path.exists('main.py')
	assert os.path.exists('models.py')
	assert os.path.exists('routes.py')
	assert os.path.exists('services.py')
	assert os.path.exists('requirements.txt')
