class Config:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = 'super-secret-key'
