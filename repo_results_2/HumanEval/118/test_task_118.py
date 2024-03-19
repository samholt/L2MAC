import pytest
from task_118 import get_closest_vowel

def test_get_closest_vowel():
	assert get_closest_vowel('yogurt') == 'u'
	assert get_closest_vowel('FULL') == 'U'
	assert get_closest_vowel('quick') == ''
	assert get_closest_vowel('ab') == ''
	assert get_closest_vowel('bcdfg') == ''
	assert get_closest_vowel('aei') == ''
	assert get_closest_vowel('bUb') == 'U'
	assert get_closest_vowel('bAbUb') == 'U'
	assert get_closest_vowel('bAbUbE') == 'U'
	assert get_closest_vowel('bAbUbEc') == 'E'
