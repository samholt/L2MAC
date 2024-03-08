from recommendations import Recommendations

def test_savings_tips():
	user = 'test_user'
	rec = Recommendations(user)
	tips = rec.savings_tips()
	assert len(tips) > 0, 'No savings tips returned'


def test_product_recommendations():
	user = 'test_user'
	rec = Recommendations(user)
	products = rec.product_recommendations()
	assert len(products) > 0, 'No product recommendations returned'
