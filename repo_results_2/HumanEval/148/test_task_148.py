import pytest
from task_148 import bf

def test_bf():
	assert bf('Jupiter', 'Neptune') == ('Saturn', 'Uranus')
	assert bf('Earth', 'Mercury') == ('Venus',)
	assert bf('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
	assert bf('Invalid', 'Planet') == ()
