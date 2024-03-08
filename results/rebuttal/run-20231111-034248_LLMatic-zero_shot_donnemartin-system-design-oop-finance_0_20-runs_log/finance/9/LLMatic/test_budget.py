import pytest
from budget import Budget, BudgetManager
from transaction import Transaction
from datetime import datetime


def test_budget():
	budget = Budget('Groceries', 200)
	transaction = Transaction('Groceries', 50, datetime.now(), 'debit')
	budget.add_transaction(transaction)
	assert budget.get_total_spent() == 50
	assert budget.get_remaining_budget() == 150
	assert not budget.is_budget_exceeded()

	transaction = Transaction('Groceries', 200, datetime.now(), 'debit')
	budget.add_transaction(transaction)
	assert budget.get_total_spent() == 250
	assert budget.get_remaining_budget() == -50
	assert budget.is_budget_exceeded()


def test_budget_manager():
	manager = BudgetManager()
	budget1 = Budget('Groceries', 200)
	budget2 = Budget('Rent', 800)
	manager.add_budget(budget1)
	manager.add_budget(budget2)
	assert manager.get_budget('Groceries') == budget1
	assert manager.get_budget('Rent') == budget2
	assert manager.get_total_budget() == 1000
	assert manager.get_total_spent() == 0
	assert manager.get_remaining_budget() == 1000

	transaction = Transaction('Groceries', 50, datetime.now(), 'debit')
	budget1.add_transaction(transaction)
	assert manager.get_total_spent() == 50
	assert manager.get_remaining_budget() == 950

	manager.delete_budget('Groceries')
	assert manager.get_budget('Groceries') is None
	assert manager.get_total_budget() == 800
	assert manager.get_total_spent() == 0
	assert manager.get_remaining_budget() == 800
