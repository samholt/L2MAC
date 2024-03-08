import re


def test_css_js_links():
	with open('templates/home.html', 'r') as f:
		home_html = f.read()
	with open('templates/register.html', 'r') as f:
		register_html = f.read()
	with open('templates/profile.html', 'r') as f:
		profile_html = f.read()

	assert re.search(r'<link rel="stylesheet" href="../static/style.css">', home_html)
	assert re.search(r'<script src="../static/theme.js"></script>', home_html)

	assert re.search(r'<link rel="stylesheet" href="../static/style.css">', register_html)
	assert re.search(r'<script src="../static/theme.js"></script>', register_html)

	assert re.search(r'<link rel="stylesheet" href="../static/style.css">', profile_html)
	assert re.search(r'<script src="../static/theme.js"></script>', profile_html)
