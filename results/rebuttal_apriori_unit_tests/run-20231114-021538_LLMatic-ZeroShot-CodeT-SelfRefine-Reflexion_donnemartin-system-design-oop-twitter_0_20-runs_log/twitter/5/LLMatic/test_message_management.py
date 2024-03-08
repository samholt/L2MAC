import pytest
import random
import string
from message_management import send_message


def random_string(length=10):
	"""Generates a random string of specified length."""
	return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def test_direct_messaging():
	sender_id = random.randint(1, 1000)
	receiver_id = random.randint(1, 1000)
	message = random_string(100)

	assert send_message(sender_id, receiver_id, message) == True
