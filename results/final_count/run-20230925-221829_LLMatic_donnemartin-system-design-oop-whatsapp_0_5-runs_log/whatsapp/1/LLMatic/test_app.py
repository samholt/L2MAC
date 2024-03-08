import pytest
from flask import Flask, request
from app import app

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_message(client):
	response = client.post('/message', json={'sender': 'test', 'receiver': 'test', 'content': 'Hello'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Message sent successfully'}


def test_post_status(client):
	response = client.post('/post_status', json={'username': 'test', 'password': 'test', 'image': 'image.jpg', 'visibility': '1'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Status posted successfully'}
