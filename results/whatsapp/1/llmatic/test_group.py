import pytest
from user import User
from group import Group

def test_create_group():
	user = User()
	user.register('test@test.com', 'password')
	group = Group()
	group.create_group('Test Group', 'test.jpg', user)
	assert group.name == 'Test Group'
	assert group.picture == 'test.jpg'
	assert group.participants == [user]
	assert group.admins == [user]

def test_add_remove_participant():
	user1 = User()
	user1.register('test1@test.com', 'password')
	user2 = User()
	user2.register('test2@test.com', 'password')
	group = Group()
	group.create_group('Test Group', 'test.jpg', user1)
	group.add_participant(user2)
	assert group.participants == [user1, user2]
	group.remove_participant(user2)
	assert group.participants == [user1]

def test_add_remove_admin():
	user1 = User()
	user1.register('test1@test.com', 'password')
	user2 = User()
	user2.register('test2@test.com', 'password')
	group = Group()
	group.create_group('Test Group', 'test.jpg', user1)
	group.add_participant(user2)
	group.add_admin(user2)
	assert group.admins == [user1, user2]
	group.remove_admin(user2)
	assert group.admins == [user1]
