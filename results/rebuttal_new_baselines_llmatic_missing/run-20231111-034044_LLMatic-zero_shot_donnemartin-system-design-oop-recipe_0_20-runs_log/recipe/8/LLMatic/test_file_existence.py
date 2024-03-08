import os

def test_file_existence():
	assert os.path.exists('app.py')
	assert os.path.exists('recipes.py')
	assert os.path.exists('users.py')
	assert os.path.exists('reviews.py')
	assert os.path.exists('categories.py')
	assert os.path.exists('admin.py')
	assert os.path.exists('recommendations.py')
	assert os.path.exists('database.py')
	assert os.path.exists('requirements.txt')
