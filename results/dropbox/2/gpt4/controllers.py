from models import User, File, Permission, UserSchema, FileSchema, PermissionSchema
from app import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)
file_schema = FileSchema()
files_schema = FileSchema(many=True)
permission_schema = PermissionSchema()
permissions_schema = PermissionSchema(many=True)

class UserController:
	@staticmethod
	def create(user):
		new_user = User(user['name'], user['email'])
		db.session.add(new_user)
		db.session.commit()
		return user_schema.dump(new_user)

	@staticmethod
	def get(id):
		user = User.query.get(id)
		return user_schema.dump(user)

class FileController:
	@staticmethod
	def upload(file):
		new_file = File(file['name'], file['content'], file['owner_id'])
		db.session.add(new_file)
		db.session.commit()
		return file_schema.dump(new_file)

	@staticmethod
	def download(id):
		file = File.query.get(id)
		return file_schema.dump(file)

	@staticmethod
	def delete(id):
		file = File.query.get(id)
		db.session.delete(file)
		db.session.commit()
		return {'message': 'File deleted'}

	@staticmethod
	def search(query):
		files = File.query.filter(File.name.contains(query)).all()
		return files_schema.dump(files)

class PermissionController:
	@staticmethod
	def share(id, permission):
		new_permission = Permission(id, permission['user_id'], permission['can_edit'], permission['can_view'])
		db.session.add(new_permission)
		db.session.commit()
		return permission_schema.dump(new_permission)

