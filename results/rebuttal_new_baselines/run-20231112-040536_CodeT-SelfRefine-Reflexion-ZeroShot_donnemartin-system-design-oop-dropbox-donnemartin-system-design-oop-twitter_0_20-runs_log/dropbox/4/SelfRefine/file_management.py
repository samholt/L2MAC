from dataclasses import dataclass
from db import db

class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	type = db.Column(db.String(50))
	size = db.Column(db.Integer)


def upload(data):
	file = File(name=data['name'], type=data['type'], size=data['size'])
	db.session.add(file)
	db.session.commit()
	return {'message': 'File uploaded successfully'}, 201

def download(data):
	file = File.query.filter_by(name=data['name']).first()
	if file:
		return {'message': 'File download endpoint'}, 200
	return {'message': 'File not found'}, 404

def organize(data):
	return {'message': 'File organize endpoint'}, 200

def get_versions():
	return {'message': 'File versioning endpoint'}, 200

def restore_version(data):
	return {'message': 'File version restore endpoint'}, 200
