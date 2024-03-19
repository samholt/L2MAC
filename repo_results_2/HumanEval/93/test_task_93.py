import pytest
from task_93 import encode

def test_encode():
	assert encode('test') == 'TGST'
	assert encode('This is a message') == 'tHKS KS C MGSSCGG'
	assert encode('aeiou') == 'CGKQW'
	assert encode('AEIOU') == 'cgkqw'
	assert encode('yY') == 'Aa'
