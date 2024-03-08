import pytest
from voting_system import VotingSystem

def test_create_voting_system():
	vs = VotingSystem(None, None)
	vs.create_voting_system('1', 'Book Club 1')
	assert vs.id == '1'
	assert vs.book_club == 'Book Club 1'
	assert vs.book_options == []

def test_add_book_option():
	vs = VotingSystem('1', 'Book Club 1')
	vs.add_book_option('Book 1')
	assert vs.book_options == ['Book 1']

def test_update_voting_system():
	vs = VotingSystem('1', 'Book Club 1', ['Book 1'])
	vs.update_voting_system(id='2', book_club='Book Club 2', book_options=['Book 2'])
	assert vs.id == '2'
	assert vs.book_club == 'Book Club 2'
	assert vs.book_options == ['Book 2']
