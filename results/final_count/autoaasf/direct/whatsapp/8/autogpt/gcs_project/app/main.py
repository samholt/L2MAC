from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .views import app
from .models import db


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gcs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'


db.init_app(app)


migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
