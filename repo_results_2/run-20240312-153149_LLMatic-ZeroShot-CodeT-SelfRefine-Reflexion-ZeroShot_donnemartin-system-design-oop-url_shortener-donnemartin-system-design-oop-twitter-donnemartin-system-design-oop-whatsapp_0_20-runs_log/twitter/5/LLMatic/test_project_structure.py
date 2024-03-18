import os

def test_project_structure():
	assert os.path.exists('app.py')
	assert os.path.exists('user_management.py')
	assert os.path.exists('post_management.py')
	assert os.path.exists('social_interaction.py')
	assert os.path.exists('trending_discovery.py')
	assert os.path.exists('requirements.txt')
