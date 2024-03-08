import pytest
from cloudsafe.app import create_app, db
from cloudsafe.app.models import User, File
from flask import url_for
from io import BytesIO


@pytest.fixture
def client():
	app = create_app()
	app.config['TESTING'] = True

	with app.test_client() as client:
		yield client

	with app.app_context():
		db.drop_all()


def test_upload_file(client):
	user = User(username='test', email='test@test.com')
	db.session.add(user)
	db.session.commit()

	response = client.post(url_for('file.upload_file'), data={'file': (BytesIO(b'my file contents'), 'my_file.txt'), 'username': 'test'}, content_type='multipart/form-data')
	assert response.status_code == 204


def test_upload_existing_file(client):
	user = User(username='test', email='test@test.com')
	db.session.add(user)
	db.session.commit()

	client.post(url_for('file.upload_file'), data={'file': (BytesIO(b'my file contents'), 'my_file.txt'), 'username': 'test'}, content_type='multipart/form-data')
	response = client.post(url_for('file.upload_file'), data={'file': (BytesIO(b'my file contents'), 'my_file.txt'), 'username': 'test'}, content_type='multipart/form-data')
	assert response.status_code == 204

	file = File.query.filter_by(filename='my_file.txt').first()
	assert len(file.versions) == 1
