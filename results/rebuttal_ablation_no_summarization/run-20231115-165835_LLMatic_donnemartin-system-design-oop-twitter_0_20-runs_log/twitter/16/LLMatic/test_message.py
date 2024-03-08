import message
import datetime


def test_send():
	m = message.Message()
	m.send('Alice', 'Bob', 'Hello, Bob!')
	assert any(text == 'Hello, Bob!' for text, _ in m.database['Alice']['Bob'])


def test_block():
	m = message.Message()
	m.block('Alice', 'Bob')
	assert m.database['Alice']['Bob'] == 'blocked'

