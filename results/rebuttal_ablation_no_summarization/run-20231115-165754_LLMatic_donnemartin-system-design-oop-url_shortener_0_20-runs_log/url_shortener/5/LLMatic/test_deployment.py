import os
import subprocess
import pytest


def test_requirements():
	assert os.path.exists('requirements.txt'), 'requirements.txt does not exist'


def test_flask_installation():
	result = subprocess.run(['pip', 'show', 'flask'], stdout=subprocess.PIPE)
	assert 'Name: Flask' in result.stdout.decode(), 'Flask is not installed'


def test_requests_installation():
	result = subprocess.run(['pip', 'show', 'requests'], stdout=subprocess.PIPE)
	assert 'Name: requests' in result.stdout.decode(), 'requests is not installed'


def test_pytest_installation():
	result = subprocess.run(['pip', 'show', 'pytest'], stdout=subprocess.PIPE)
	assert 'Name: pytest' in result.stdout.decode(), 'pytest is not installed'


def test_app_running():
	try:
		subprocess.check_output(['python', 'app.py'], timeout=5)
	except subprocess.CalledProcessError as e:
		if 'Address already in use' in str(e):
			pass
		elif 'Error: While importing' in str(e):
			pytest.fail(f'App failed to start with error: {str(e)}')
	except subprocess.TimeoutExpired:
		# If the app is running correctly, it should timeout because it's a long running process
		pass

