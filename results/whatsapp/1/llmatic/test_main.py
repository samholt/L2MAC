import pytest
from main import *


def test_main():
	app = WebApp()
	app.register_user('test@example.com', 'password')
	assert app.login_user('test@example.com', 'password') is not None
	app.send_message('test@example.com', 'recipient@example.com', 'Hello, world!', 'text')
	app.restore_connectivity('test@example.com')
	assert app.display_status('test@example.com') is not None


def test_main_fail():
	app = WebApp()
	app.register_user('test@example.com', 'password')
	assert app.login_user('wrong@example.com', 'password') is None
	app.send_message('test@example.com', 'recipient@example.com', 'Hello, world!', 'text')
	app.restore_connectivity('test@example.com')
	assert app.display_status('wrong@example.com') is None
