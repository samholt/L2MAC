import sys
sys.path.append('..')

import pytest
from url_shortener.validator import is_valid_url

def test_is_valid_url():
	assert is_valid_url('https://www.google.com') == True
	assert is_valid_url('https://www.thisurldoesnotexist.com') == False
