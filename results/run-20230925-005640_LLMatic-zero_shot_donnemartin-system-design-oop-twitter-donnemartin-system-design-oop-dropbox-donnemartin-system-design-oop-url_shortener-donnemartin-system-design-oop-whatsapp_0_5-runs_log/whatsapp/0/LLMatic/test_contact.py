import pytest
from contact import Contact
from user import User

def test_block():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	contact = Contact(user1, user2)
	contact.block()
	assert contact.blocked == True

def test_unblock():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	contact = Contact(user1, user2)
	contact.block()
	contact.unblock()
	assert contact.blocked == False
