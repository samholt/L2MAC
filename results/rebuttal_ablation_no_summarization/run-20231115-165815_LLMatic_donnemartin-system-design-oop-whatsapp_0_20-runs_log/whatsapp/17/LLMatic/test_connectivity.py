import pytest
from connectivity import Connectivity


def test_connectivity():
	connectivity = Connectivity()
	connectivity.go_online('user1')
	assert connectivity.send_message('user1', 'user2', 'Hello') == False
	connectivity.go_online('user2')
	assert connectivity.send_message('user1', 'user2', 'Hello') == True
	connectivity.go_offline('user2')
	assert connectivity.send_message('user1', 'user2', 'Hello') == False
