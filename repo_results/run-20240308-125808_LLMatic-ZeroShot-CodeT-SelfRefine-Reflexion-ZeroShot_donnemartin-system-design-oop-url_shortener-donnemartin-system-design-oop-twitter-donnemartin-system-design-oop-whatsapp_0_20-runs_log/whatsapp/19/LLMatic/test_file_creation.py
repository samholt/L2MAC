import os

def test_file_creation():
	assert os.path.exists('app.py')
	assert os.path.exists('config.py')
	assert os.path.exists('user.py')
	assert os.path.exists('message.py')
	assert os.path.exists('group.py')
	assert os.path.exists('status.py')
	assert os.path.exists('requirements.txt')
