import pytest
from voting_system import VotingSystem

def test_voting_system():
	vs = VotingSystem('1', ['Option 1', 'Option 2'])
	assert vs.get_info() == {'id': '1', 'options': ['Option 1', 'Option 2'], 'votes': {'Option 1': 0, 'Option 2': 0}}

	vs.add_option('Option 3')
	assert vs.get_info() == {'id': '1', 'options': ['Option 1', 'Option 2', 'Option 3'], 'votes': {'Option 1': 0, 'Option 2': 0, 'Option 3': 0}}

	vs.remove_option('Option 2')
	assert vs.get_info() == {'id': '1', 'options': ['Option 1', 'Option 3'], 'votes': {'Option 1': 0, 'Option 3': 0}}

	vs.cast_vote('Option 1')
	assert vs.get_info() == {'id': '1', 'options': ['Option 1', 'Option 3'], 'votes': {'Option 1': 1, 'Option 3': 0}}
