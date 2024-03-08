from models.message import Message
from services.message_service import MessageService

def test_message_service():
	message_service = MessageService()
	message_service.send_message('1', 'sender', 'receiver', 'content')
	message = message_service.receive_message('1')
	assert message.id == '1'
	assert message.sender == 'sender'
	assert message.receiver == 'receiver'
	assert message.content == 'content'
	assert message.read_receipt == False
	assert message.encryption == False

	message_service.set_read_receipt('1')
	message = message_service.receive_message('1')
	assert message.read_receipt == True

	message_service.encrypt_message('1')
	message = message_service.receive_message('1')
	assert message.content == 'encrypted'
	assert message.encryption == True

	message_service.share_image('1', 'image')
	message = message_service.receive_message('1')
	assert message.content == 'encryptedimage'
