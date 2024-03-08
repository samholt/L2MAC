import pytest
from cloudsafe.controllers.user_controller import user_controller

def test_register():
	response = user_controller.register()
	assert response.status_code == 201

def test_login():
	response = user_controller.login()
	assert response.status_code == 200

def test_update_profile():
	response = user_controller.update_profile()
	assert response.status_code == 200

def test_calculate_storage_used():
	response = user_controller.calculate_storage_used()
	assert response.status_code == 200
