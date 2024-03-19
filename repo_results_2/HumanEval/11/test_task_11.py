import pytest
from task_11 import string_xor

def test_string_xor():
	assert string_xor('010', '110') == '100'
	assert string_xor('1', '1') == '0'
	assert string_xor('0', '0') == '0'
	assert string_xor('1111', '0000') == '1111'
	assert string_xor('1010', '0101') == '1111'
	assert string_xor('1111', '1111') == '0000'
	assert string_xor('0000', '0000') == '0000'
	assert string_xor('10101010', '01010101') == '11111111'
	assert string_xor('11111111', '11111111') == '00000000'
	assert string_xor('00000000', '00000000') == '00000000'
