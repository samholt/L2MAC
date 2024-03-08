import user


def test_get_savings_tips():
	user.create_user('test_user', 'password', 'test_user@example.com')
	tips = user.get_savings_tips('test_user')
	assert tips == ['Tip 1', 'Tip 2', 'Tip 3'], 'get_savings_tips function not working correctly'


def test_get_product_recommendations():
	user.create_user('test_user', 'password', 'test_user@example.com')
	products = user.get_product_recommendations('test_user')
	assert products == ['Product 1', 'Product 2', 'Product 3'], 'get_product_recommendations function not working correctly'

