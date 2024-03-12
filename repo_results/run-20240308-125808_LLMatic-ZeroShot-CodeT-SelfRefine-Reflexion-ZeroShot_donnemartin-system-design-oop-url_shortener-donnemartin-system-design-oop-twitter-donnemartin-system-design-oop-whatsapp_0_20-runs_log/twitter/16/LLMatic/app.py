from flask import Flask, render_template
from models import db
import views

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = 'supersecretkey'

db.init_app(app)

app.register_blueprint(views.bp)

@app.before_request
def create_tables():
	db.create_all()

if __name__ == '__main__':
	app.run(debug=True)
