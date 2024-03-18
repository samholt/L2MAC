import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('requirements.txt')
	assert os.path.exists('models')
	assert os.path.exists('routes')
	assert os.path.exists('tests')
