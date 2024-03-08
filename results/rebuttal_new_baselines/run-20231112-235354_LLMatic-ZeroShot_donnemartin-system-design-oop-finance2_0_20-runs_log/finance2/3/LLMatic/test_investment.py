import pytest
from models.investment import Investment

def test_investment_model():
	investment = Investment('user1', 1000, 'stocks')
	investment.link_investment_account('account1')
	assert investment.account == 'account1'
	assert investment.track_investment_performance() == {'status': 'success', 'message': 'Investment performance tracked successfully'}
	assert investment.get_user_investments() == [{'investment_type': 'stocks', 'investment_amount': 1000}]
