import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('url_shortener.py')
	assert os.path.exists('user.py')
	assert os.path.exists('admin.py')
	assert os.path.exists('analytics.py')
	assert os.path.exists('database.py')
	assert os.path.exists('requirements.txt')
