import pytest
import status
import datetime
import time

def test_status_expiration():
	status_instance = status.Status('user1', 'Hello World!', 'public', 5)
	assert not status_instance.is_expired()
	time.sleep(6)
	assert status_instance.is_expired()
