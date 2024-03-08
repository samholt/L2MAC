import os

def test_project_structure():
	assert os.path.exists('main.py')
	assert os.path.exists('models.py')
	assert os.path.exists('views.py')
	assert os.path.exists('utils.py')
	assert os.path.exists('requirements.txt')
