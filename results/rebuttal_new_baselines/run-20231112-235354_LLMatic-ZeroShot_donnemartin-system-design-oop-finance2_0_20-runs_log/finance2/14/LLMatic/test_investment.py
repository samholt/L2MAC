import pytest
from models.investment import Investment
from models.user import User

def test_create_investment():
	user = User('user1', 'user1@email.com', 'password')
	investment = Investment.create_investment(user, 1000, 'Stocks')
	assert investment.user == user
	assert investment.amount == 1000
	assert investment.type == 'Stocks'

def test_get_user_investments():
	user = User('user1', 'user1@email.com', 'password')
	investments = Investment.get_user_investments(user)
	assert len(investments) == 2
	assert investments[0].user == user
	assert investments[0].amount == 1000
	assert investments[0].type == 'Stocks'
	assert investments[1].user == user
	assert investments[1].amount == 2000
	assert investments[1].type == 'Bonds'

def test_track_performance():
	user = User('user1', 'user1@email.com', 'password')
	investment = Investment(user, 1000, 'Stocks')
	performance = investment.track_performance()
	assert performance['investment'] == investment.serialize()
	assert performance['performance'] == 'Good'
