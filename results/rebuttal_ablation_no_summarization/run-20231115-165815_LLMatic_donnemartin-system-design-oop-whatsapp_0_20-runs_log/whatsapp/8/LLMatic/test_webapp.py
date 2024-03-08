import pytest
from webapp import WebApp

def test_webapp():
	webapp = WebApp()
	assert webapp is not None

	# Test display_user_interface method
	webapp.display_user_interface()

	# Test handle_user_input method
	webapp.handle_user_input('test input')
