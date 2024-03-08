from flask import Flask
from .routes import security_bp

app = Flask(__name__)
app.register_blueprint(security_bp)
