import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('requirements.txt')
	assert os.path.exists('models/User.py')
	assert os.path.exists('models/File.py')
	assert os.path.exists('routes/user_routes.py')
	assert os.path.exists('routes/file_routes.py')
	assert os.path.exists('services/user_service.py')
	assert os.path.exists('services/file_service.py')
