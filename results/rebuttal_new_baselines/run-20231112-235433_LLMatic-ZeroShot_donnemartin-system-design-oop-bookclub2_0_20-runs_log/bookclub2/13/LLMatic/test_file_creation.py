import os

def test_file_creation():
	assert os.path.exists('app.py')
	assert os.path.exists('book_club.py')
	assert os.path.exists('meeting.py')
	assert os.path.exists('discussion.py')
	assert os.path.exists('user.py')
	assert os.path.exists('admin.py')
	assert os.path.exists('database.py')
	assert os.path.exists('requirements.txt')
