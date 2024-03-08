import pytest
import app
from flask import Flask, request

app_obj = Flask(__name__)


def test_create_club_missing_data():
	with app_obj.test_request_context('/create_club', json={}):
		response = app.create_club()
		assert response[1] == 400


def test_join_club_missing_data():
	with app_obj.test_request_context('/join_club', json={}):
		response = app.join_club()
		assert response[1] == 400


def test_schedule_meeting_missing_data():
	with app_obj.test_request_context('/schedule_meeting', json={}):
		response = app.schedule_meeting()
		assert response[1] == 400


def test_create_forum_missing_data():
	with app_obj.test_request_context('/create_forum', json={}):
		response = app.create_forum()
		assert response[1] == 400


def test_create_user_missing_data():
	with app_obj.test_request_context('/create_user', json={}):
		response = app.create_user()
		assert response[1] == 400


def test_access_dashboard_server_error():
	with app_obj.test_request_context('/access_dashboard', json={}):
		response = app.access_dashboard()
		assert response[1] == 200

