import user


def test_provide_savings_tips():
	user.create_user('testuser', 'password', 'testuser@example.com')
	assert user.provide_savings_tips('testuser') == 'Save money by reducing your spending on non-essential items'
	assert user.provide_savings_tips('nonexistentuser') == 'Username does not exist'


def test_recommend_financial_products():
	user.create_user('testuser2', 'password', 'testuser2@example.com')
	assert user.recommend_financial_products('testuser2') == 'Based on your profile, we recommend investing in a low-risk mutual fund'
	assert user.recommend_financial_products('nonexistentuser') == 'Username does not exist'
