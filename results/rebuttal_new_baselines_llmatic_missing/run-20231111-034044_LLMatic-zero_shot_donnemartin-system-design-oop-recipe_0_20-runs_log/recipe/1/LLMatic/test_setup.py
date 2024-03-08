import pytest
import pkg_resources

def test_dependencies():
	assert pkg_resources.get_distribution('flask')
	assert pkg_resources.get_distribution('pytest')
