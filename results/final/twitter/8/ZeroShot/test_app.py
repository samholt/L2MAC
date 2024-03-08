import pytest
from app import app, db
from models import User


def setup_module(module):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	db.create_all()


def teardown_module(module):
	db.session.remove()
	db.drop_all()


def test_register():
	pass


def test_login():
	pass


def test_profile():
	pass


def test_post():
	pass


def test_interact():
	pass


def test_search():
	pass


def test_follow():
	pass


def test_message():
	pass


def test_notification():
	pass


def test_trending():
	pass


def test_recommendation():
	pass
