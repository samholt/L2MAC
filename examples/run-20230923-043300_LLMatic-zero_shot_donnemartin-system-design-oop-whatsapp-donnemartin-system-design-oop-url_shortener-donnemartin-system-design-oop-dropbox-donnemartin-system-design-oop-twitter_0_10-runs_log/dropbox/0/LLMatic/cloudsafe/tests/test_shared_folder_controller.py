import pytest
from cloudsafe.controllers.shared_folder_controller import shared_folder_controller

def test_invite_user():
	response = shared_folder_controller.invite_user()
	assert response.status_code == 201

def test_set_permissions():
	response = shared_folder_controller.set_permissions()
	assert response.status_code == 200
