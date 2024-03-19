import pytest
from task_154 import cycpattern_check

def test_cycpattern_check():
	assert cycpattern_check('abcd', 'abd') == False
	assert cycpattern_check('hello', 'ell') == True
	assert cycpattern_check('whassup', 'psus') == False
	assert cycpattern_check('abab', 'baa') == True
	assert cycpattern_check('efef', 'eeff') == False
	assert cycpattern_check('himenss', 'simen') == True
	assert cycpattern_check('', 'simen') == False
	assert cycpattern_check('himenss', '') == True
	assert cycpattern_check('', '') == True
	assert cycpattern_check('abcd', 'abcd') == True
	assert cycpattern_check('abcd', 'dcba') == False
