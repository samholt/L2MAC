import pytest
from recommendations import Recommendations

def test_add_and_get_recommendation():
	rec = Recommendations()
	rec.add_recommendation('user1', 'Invest in stocks')
	assert rec.get_recommendations('user1') == ['Invest in stocks']


def test_add_and_get_savings_tip():
	rec = Recommendations()
	rec.add_savings_tip('user1', 'Save 20% of your income')
	assert rec.get_savings_tips('user1') == ['Save 20% of your income']
