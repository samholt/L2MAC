import os
import pytest

def test_project_files():
	assert os.path.exists('main.py')
	assert os.path.exists('requirements.txt')

def test_dependencies():
	try:
		import flask
		import pytest
		import dataclasses
	except ImportError:
		pytest.fail('One or more dependencies are not installed.')
