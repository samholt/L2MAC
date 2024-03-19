import pytest
from task_124 import valid_date

def test_valid_date():
	assert valid_date('03-11-2000') == True
	assert valid_date('15-01-2012') == False
	assert valid_date('04-0-2040') == False
	assert valid_date('06-04-2020') == True
	assert valid_date('06/04/2020') == False
	assert valid_date('02-30-2000') == False
	assert valid_date('04-31-2000') == False
	assert valid_date('06-31-2000') == False
	assert valid_date('09-31-2000') == False
	assert valid_date('11-31-2000') == False
