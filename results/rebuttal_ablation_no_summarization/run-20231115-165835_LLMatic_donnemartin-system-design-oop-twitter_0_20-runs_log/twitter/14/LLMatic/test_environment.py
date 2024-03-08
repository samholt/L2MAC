def test_environment_setup():
	with open('requirements.txt', 'r') as f:
		requirements = f.read().splitlines()
	assert 'Flask' in requirements
	assert 'Pytest' in requirements
	assert 'PyJWT' in requirements
