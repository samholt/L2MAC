from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import bp as routes_bp

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

app.register_blueprint(routes_bp)
