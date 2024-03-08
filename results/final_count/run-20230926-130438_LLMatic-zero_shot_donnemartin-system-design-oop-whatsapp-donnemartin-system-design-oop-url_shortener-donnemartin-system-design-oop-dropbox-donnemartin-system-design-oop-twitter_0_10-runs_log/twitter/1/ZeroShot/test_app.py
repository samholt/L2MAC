import pytest
from app import app, db
from models import User, Post, Comment, Like, Follow, Message


def setup_module(module):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
	db.create_all()


def teardown_module(module):
	db.session.remove()
	db.drop_all()


def test_register():
	# TODO: Implement registration test
	pass


def test_login():
	# TODO: Implement login test
	pass


def test_profile():
	# TODO: Implement profile view/edit test
	pass


def test_create_post():
	# TODO: Implement post creation test
	pass


def test_post():
	# TODO: Implement post view/delete test
	pass


def test_like_post():
	# TODO: Implement post like test
	pass


def test_comment_post():
	# TODO: Implement post comment test
	pass


def test_follow():
	# TODO: Implement follow test
	pass


def test_message():
	# TODO: Implement direct message test
	pass


def test_trending():
	# TODO: Implement trending topics test
	pass
