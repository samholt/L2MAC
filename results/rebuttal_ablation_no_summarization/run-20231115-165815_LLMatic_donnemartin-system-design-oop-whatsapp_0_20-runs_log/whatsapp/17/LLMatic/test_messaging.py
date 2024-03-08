from messaging import Messaging, Message

def test_send_message():
	messaging = Messaging()
	messaging.send_message('Alice', 'Bob', 'Hello, Bob!')
	assert len(messaging.messages) == 1
	assert messaging.messages[0].sender == 'Alice'
	assert messaging.messages[0].receiver == 'Bob'
	assert messaging.messages[0].content == 'Hello, Bob!'


def test_read_message():
	messaging = Messaging()
	messaging.send_message('Alice', 'Bob', 'Hello, Bob!')
	message = messaging.messages[0]
	messaging.read_message(message)
	assert message.read


def test_encrypt_decrypt_message():
	messaging = Messaging()
	messaging.send_message('Alice', 'Bob', 'Hello, Bob!')
	message = messaging.messages[0]
	messaging.encrypt_message(message)
	assert message.content == '!boB ,olleH'
	assert message.encrypted
	messaging.decrypt_message(message)
	assert message.content == 'Hello, Bob!'
	assert not message.encrypted
