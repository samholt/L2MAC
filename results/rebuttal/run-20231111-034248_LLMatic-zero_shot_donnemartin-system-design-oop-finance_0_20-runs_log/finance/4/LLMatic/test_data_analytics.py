import pytest
from data import Data

def test_generate_monthly_report():
	data = Data()
	data.add_transaction('user1', 100, 'income', 1, 2022)
	data.add_transaction('user1', -50, 'groceries', 1, 2022)
	report = data.generate_monthly_report('user1', 1, 2022)
	assert report == {}

def test_provide_spending_habits():
	data = Data()
	data.add_transaction('user1', -50, 'groceries', 1, 2022)
	data.add_transaction('user1', -30, 'entertainment', 1, 2022)
	spending_habits = data.provide_spending_habits('user1')
	assert spending_habits == {}

def test_compare_year_on_year():
	data = Data()
	data.add_transaction('user1', 100, 'income', 12, 2021)
	data.add_transaction('user1', 200, 'income', 12, 2022)
	comparison = data.compare_year_on_year('user1', 2021, 2022)
	assert comparison == {}
