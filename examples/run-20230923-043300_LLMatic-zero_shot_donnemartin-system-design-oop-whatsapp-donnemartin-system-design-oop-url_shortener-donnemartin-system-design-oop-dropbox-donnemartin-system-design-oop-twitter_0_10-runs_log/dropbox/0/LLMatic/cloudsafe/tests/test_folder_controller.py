import pytest
from cloudsafe.controllers.folder_controller import folder_controller

def test_create():
	response = folder_controller.create()
	assert response.status_code == 201

def test_rename():
	response = folder_controller.rename()
	assert response.status_code == 200

def test_move():
	response = folder_controller.move()
	assert response.status_code == 200

def test_delete():
	response = folder_controller.delete()
	assert response.status_code == 200
