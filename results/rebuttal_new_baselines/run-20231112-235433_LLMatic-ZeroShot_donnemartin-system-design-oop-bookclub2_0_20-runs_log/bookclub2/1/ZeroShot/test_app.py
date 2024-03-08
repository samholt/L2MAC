import pytest
import app
from app import User, Club, Meeting, Discussion


def test_create_user():
	user = User(id='1', name='John Doe', clubs=[], reading_list=[], recommendations=[])
	app.users[user.id] = user
	assert app.users[user.id] == user


def test_create_club():
	club = Club(id='1', name='Book Club', members=[], privacy='public', admin='1')
	app.clubs[club.id] = club
	assert app.clubs[club.id] == club


def test_create_meeting():
	meeting = Meeting(id='1', club_id='1', date='2022-12-31', reminder=False)
	app.meetings[meeting.id] = meeting
	assert app.meetings[meeting.id] == meeting


def test_create_discussion():
	discussion = Discussion(id='1', club_id='1', book='Book 1', comments=[])
	app.discussions[discussion.id] = discussion
	assert app.discussions[discussion.id] == discussion
