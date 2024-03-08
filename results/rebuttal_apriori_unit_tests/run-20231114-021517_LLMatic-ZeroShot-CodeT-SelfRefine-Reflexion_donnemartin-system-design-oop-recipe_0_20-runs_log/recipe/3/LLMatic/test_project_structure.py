import os


def test_project_structure():
	assert os.path.exists('recipe_platform.py')
	assert os.path.exists('requirements.txt')
