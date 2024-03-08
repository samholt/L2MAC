import os


def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('models/user.py')
	assert os.path.exists('models/file.py')
	assert os.path.exists('services/user_service.py')
	assert os.path.exists('services/file_service.py')
	assert os.path.exists('services/share_service.py')
	assert os.path.exists('requirements.txt')
