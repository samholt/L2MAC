from flask import Flask, session
from user_management.routes import user_management
from file_management.routes import file_management
from file_sharing.routes import file_sharing
from security.routes import security_bp

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(user_management)
app.register_blueprint(file_management)
app.register_blueprint(file_sharing)
app.register_blueprint(security_bp)

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
