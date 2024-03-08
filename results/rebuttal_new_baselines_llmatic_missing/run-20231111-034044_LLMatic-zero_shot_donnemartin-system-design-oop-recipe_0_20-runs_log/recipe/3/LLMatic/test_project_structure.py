import os

def test_main_py_exists():
	assert os.path.exists('main.py')

def test_requirements_txt_exists():
	assert os.path.exists('requirements.txt')
