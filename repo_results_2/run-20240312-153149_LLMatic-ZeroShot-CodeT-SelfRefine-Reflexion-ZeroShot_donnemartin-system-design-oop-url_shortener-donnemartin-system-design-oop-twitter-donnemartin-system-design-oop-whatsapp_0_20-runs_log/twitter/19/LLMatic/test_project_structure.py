import os

def test_project_structure():
	assert os.path.exists('user_management.py')
	assert os.path.exists('posting_content_management.py')
	assert os.path.exists('social_interaction.py')
	assert os.path.exists('trending_discovery.py')
	assert os.path.exists('main.py')
	assert os.path.exists('requirements.txt')
