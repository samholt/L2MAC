import pytest
from webapp import WebApp

def test_webapp():
	webapp = WebApp()

	# Test manage_connectivity method
	assert webapp.manage_connectivity(True) == True
	assert webapp.manage_connectivity(False) == False
