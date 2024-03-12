from message import Message

def test_message():
	message = Message('Alice', 'Bob', 'Hello, Bob!', False, '1234', 'image.jpg')

	# Test sending a message
	message.send_message('Bob', 'Hello, Bob!')

	# Test receiving a message
	message.receive_message('Alice', 'Hello, Alice!')

	# Test managing read receipt
	message.manage_read_receipt(True)

	# Test encrypting a message
	message.encrypt_message('Hello, Bob!', '1234')

	# Test decrypting a message
	message.decrypt_message('!boB ,olleH', '1234')

	# Test sharing an image
	message.share_image('image.jpg')

	# Test queuing a message
	message.queue_message('Hello, Bob!')

	# Test displaying online status
	assert message.display_online_status() == False
