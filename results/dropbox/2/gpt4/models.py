from app import db, ma

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	email = db.Column(db.String(100), unique=True)

	def __init__(self, name, email):
		self.name = name
		self.email = email

class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User
		load_instance = True


class File(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True)
	content = db.Column(db.LargeBinary)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, name, content, owner_id):
		self.name = name
		self.content = content
		self.owner_id = owner_id

class FileSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = File
		load_instance = True


class Permission(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	can_edit = db.Column(db.Boolean)
	can_view = db.Column(db.Boolean)

	def __init__(self, file_id, user_id, can_edit, can_view):
		self.file_id = file_id
		self.user_id = user_id
		self.can_edit = can_edit
		self.can_view = can_view

class PermissionSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Permission
		load_instance = True

