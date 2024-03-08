import pytest
from admin_dashboard import Admin
from database import Database


def test_admin_dashboard():
	db = Database()
	admin = Admin('1', 'Admin1')
	db.add_admin('1', admin)
	assert db.admins['1'] == admin
