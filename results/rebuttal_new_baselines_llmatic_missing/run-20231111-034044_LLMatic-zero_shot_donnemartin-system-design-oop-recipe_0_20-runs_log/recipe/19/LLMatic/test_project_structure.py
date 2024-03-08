import os

def test_main_py_exists():
	assert os.path.isfile('main.py')

def test_requirements_txt_exists():
	assert os.path.isfile('requirements.txt')
