import pytest
from cloudsafe.controllers.file_controller import file_controller

def test_upload():
	response = file_controller.upload()
	assert response.status_code == 201

def test_download():
	response = file_controller.download()
	assert response.status_code == 200

def test_rename():
	response = file_controller.rename()
	assert response.status_code == 200

def test_move():
	response = file_controller.move()
	assert response.status_code == 200

def test_delete():
	response = file_controller.delete()
	assert response.status_code == 200
