import pytest
import random
import string

from offline_service import OfflineService

offline_service = OfflineService()


def test_message_queuing():
	sender_id = random.randint(1, 100)
	receiver_id = random.randint(1, 100)
	offline_service.set_offline(receiver_id)
	message = f'Message {random.randint(1, 1000)}'
	assert offline_service.send_message(sender_id, receiver_id, message) == 'Queued'
	offline_service.set_online(receiver_id)
	assert offline_service.check_message_sent(sender_id, receiver_id) == True
