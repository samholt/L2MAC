import pytest
from book_club import BookClub

def test_create_club():
	bc = BookClub()
	assert bc.create_club('SciFi', 'public') == 'Club created successfully'
	assert bc.create_club('SciFi', 'public') == 'Club already exists'

def test_join_club():
	bc = BookClub()
	bc.create_club('SciFi', 'public')
	assert bc.join_club('SciFi', 'John') == 'User added successfully'
	assert bc.join_club('SciFi', 'John') == 'User already a member'
	assert bc.join_club('Fantasy', 'John') == 'Club does not exist'

def test_set_privacy():
	bc = BookClub()
	bc.create_club('SciFi', 'public')
	assert bc.set_privacy('SciFi', 'private') == 'Privacy setting updated'
	assert bc.set_privacy('Fantasy', 'private') == 'Club does not exist'

def test_manage_roles():
	bc = BookClub()
	bc.create_club('SciFi', 'public')
	bc.join_club('SciFi', 'John')
	assert bc.manage_roles('SciFi', 'John', 'admin') == 'Role updated'
	assert bc.manage_roles('SciFi', 'Jane', 'admin') == 'User not a member'
	assert bc.manage_roles('Fantasy', 'John', 'admin') == 'Club does not exist'
