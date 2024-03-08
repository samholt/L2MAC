from flask import Flask
from models import db
from views import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


if __name__ == '__main__':
	app.run(debug=True)
