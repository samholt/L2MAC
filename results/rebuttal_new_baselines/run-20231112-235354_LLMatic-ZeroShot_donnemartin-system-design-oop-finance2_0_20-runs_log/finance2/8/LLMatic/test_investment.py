from models.investment import Investment

def test_investment_creation():
	investment = Investment.create_investment('test_user', 1000, 'stocks')
	assert investment.user == 'test_user'
	assert investment.amount == 1000
	assert investment.type == 'stocks'


def test_get_user_investments():
	Investment.create_investment('test_user', 2000, 'bonds')
	investments = Investment.get_user_investments('test_user')
	assert len(investments) == 2
	assert investments[0].type == 'stocks'
	assert investments[1].type == 'bonds'


def test_track_investment_performance():
	performance = Investment.track_investment_performance('test_user')
	assert performance['stocks'] == 1050
	assert performance['bonds'] == 2100
