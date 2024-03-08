import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('requirements.txt')
