import pytest
from chat import Chat


def test_chat():
	chat = Chat('Test Chat')
	assert chat.name == 'Test Chat'
	assert chat.id is not None
