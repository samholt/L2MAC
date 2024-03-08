def test_deploy():
	try:
		exec(open('deploy.py').read())
	except Exception as e:
		assert False, f'Deployment script failed with error: {e}'
