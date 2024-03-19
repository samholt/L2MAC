import pytest
from task_95 import check_dict_case

def test_check_dict_case():
	assert check_dict_case({"a":"apple", "b":"banana"}) == True
	assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
	assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
	assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
	assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
	assert check_dict_case({}) == False
