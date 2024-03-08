import pytest
from cloudsafe.controllers.shared_link_controller import shared_link_controller

def test_generate_link():
	response = shared_link_controller.generate_link()
	assert response.status_code == 201

def test_set_expiry_date():
	response = shared_link_controller.set_expiry_date()
	assert response.status_code == 200

def test_set_password():
	response = shared_link_controller.set_password()
	assert response.status_code == 200
