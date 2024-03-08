from setuptools import setup, find_packages

setup(
	name='ChatApp',
	version='1.0',
	description='A simple chat application built with Flask',
	author='ChatGPT',
	author_email='chatgpt@openai.com',
	url='https://github.com/openai/chatgpt',
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		'flask',
		'flask-login',
		'flask-wtf',
		'flask-sqlalchemy',
		'flask-migrate',
		'flask-socketio',
		'flask-bootstrap',
		'flask-moment',
		'flask-bcrypt',
		'email-validator'
	],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	]
)
