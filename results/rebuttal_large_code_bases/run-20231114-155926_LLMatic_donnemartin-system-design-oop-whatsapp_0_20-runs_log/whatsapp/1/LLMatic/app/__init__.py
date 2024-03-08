from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# Initialize SQLAlchemy with Flask app
db = SQLAlchemy(app)

# Import routes after initializing db to avoid circular imports
from app import routes
