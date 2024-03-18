import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('requirements.txt')
	assert os.path.exists('user.py')
	assert os.path.exists('url.py')
	assert os.path.exists('analytics.py')
	assert os.path.exists('admin.py')
	assert os.path.exists('database.py')
