import pytest
from task_50 import encode_shift, decode_shift


def test_encode_shift():
	assert encode_shift('abc') == 'fgh'
	assert encode_shift('xyz') == 'cde'


def test_decode_shift():
	assert decode_shift('fgh') == 'abc'
	assert decode_shift('cde') == 'xyz'
