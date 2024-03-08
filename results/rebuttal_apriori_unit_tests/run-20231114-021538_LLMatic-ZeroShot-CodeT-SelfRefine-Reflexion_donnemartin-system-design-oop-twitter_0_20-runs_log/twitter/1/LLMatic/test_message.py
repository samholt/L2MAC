import pytest
from message import send_message

def test_send_message():
	assert send_message(1, 2, 'Hello') == True
