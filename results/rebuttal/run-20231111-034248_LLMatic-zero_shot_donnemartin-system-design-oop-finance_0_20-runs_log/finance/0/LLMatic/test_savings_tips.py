import pytest
from savings_tips import SavingsTips


def test_savings_tips():
	savings_tips = SavingsTips()
	assert savings_tips.add_savings_tip('user1', 'Save 10% of your income') == 'Savings tip added successfully'
	assert savings_tips.get_savings_tips('user1') == ['Save 10% of your income']
	assert savings_tips.get_savings_tips('user2') == 'No savings tips available'

