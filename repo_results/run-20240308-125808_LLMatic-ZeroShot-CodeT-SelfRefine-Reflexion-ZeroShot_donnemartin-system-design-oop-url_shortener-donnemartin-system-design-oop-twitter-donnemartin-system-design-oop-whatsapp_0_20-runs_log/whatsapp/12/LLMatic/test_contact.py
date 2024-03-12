import pytest
from contact import Contact

def test_block_unblock():
	contact = Contact('Test')
	contact.block()
	assert contact.blocked == True
	contact.unblock()
	assert contact.blocked == False
