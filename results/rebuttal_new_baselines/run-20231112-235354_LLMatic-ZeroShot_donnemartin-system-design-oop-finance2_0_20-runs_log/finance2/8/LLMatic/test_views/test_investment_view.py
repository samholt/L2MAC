from views.investment_view import InvestmentView


def test_create_investment():
	investment = InvestmentView.create_investment('user1', 1000, 'stocks')
	assert investment.user == 'user1'
	assert investment.amount == 1000
	assert investment.type == 'stocks'


def test_get_user_investments():
	InvestmentView.create_investment('user1', 1000, 'stocks')
	InvestmentView.create_investment('user1', 2000, 'bonds')
	investments = InvestmentView.get_user_investments('user1')
	assert len(investments) == 2
	assert investments[0].user == 'user1'
	assert investments[0].amount == 1000
	assert investments[0].type == 'stocks'
	assert investments[1].user == 'user1'
	assert investments[1].amount == 2000
	assert investments[1].type == 'bonds'


def test_track_investment_performance():
	InvestmentView.create_investment('user1', 1000, 'stocks')
	InvestmentView.create_investment('user1', 2000, 'bonds')
	performance = InvestmentView.track_investment_performance('user1')
	assert performance['stocks'] == 1050
	assert performance['bonds'] == 2100
