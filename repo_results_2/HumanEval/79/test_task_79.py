import pytest
from task_79 import decimal_to_binary

def test_decimal_to_binary():
	assert decimal_to_binary(0) == 'db0db'
	assert decimal_to_binary(1) == 'db1db'
	assert decimal_to_binary(2) == 'db10db'
	assert decimal_to_binary(3) == 'db11db'
	assert decimal_to_binary(4) == 'db100db'
	assert decimal_to_binary(5) == 'db101db'
	assert decimal_to_binary(6) == 'db110db'
	assert decimal_to_binary(7) == 'db111db'
	assert decimal_to_binary(8) == 'db1000db'
	assert decimal_to_binary(9) == 'db1001db'
	assert decimal_to_binary(10) == 'db1010db'

	with pytest.raises(ValueError):
		decimal_to_binary(-1)
		decimal_to_binary(1.5)
