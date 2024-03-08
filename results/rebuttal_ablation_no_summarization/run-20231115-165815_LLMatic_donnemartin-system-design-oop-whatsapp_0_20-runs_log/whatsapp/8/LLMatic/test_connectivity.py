import pytest
from connectivity import Connectivity

def test_connectivity():
	connectivity = Connectivity()
	assert connectivity.check_connectivity() == False
	connectivity.connect()
	assert connectivity.check_connectivity() == True
	connectivity.disconnect()
	assert connectivity.check_connectivity() == False

def test_queue_message():
	connectivity = Connectivity()
	connectivity.queue_message('Hello')
	assert connectivity.message_queue == ['Hello']
	connectivity.connect()
	assert connectivity.message_queue == []

def test_display_status():
	connectivity = Connectivity()
	assert connectivity.display_status() == 'Offline'
	connectivity.connect()
	assert connectivity.display_status() == 'Online'
