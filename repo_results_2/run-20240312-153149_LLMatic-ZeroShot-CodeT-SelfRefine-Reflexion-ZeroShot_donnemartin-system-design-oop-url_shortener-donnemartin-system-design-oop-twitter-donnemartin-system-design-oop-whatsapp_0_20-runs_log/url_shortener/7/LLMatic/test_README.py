import os

def test_README_exists():
	assert os.path.isfile('README.md'), 'README.md file does not exist'

def test_README_contents():
	with open('README.md', 'r') as f:
		contents = f.read()
	assert 'URL Shortener Application' in contents, 'README.md does not contain application title'
	assert 'How to Run the Application' in contents, 'README.md does not contain run instructions'
	assert 'API Usage' in contents, 'README.md does not contain API usage'
	assert 'Testing' in contents, 'README.md does not contain testing instructions'
