from flask import Flask
import views

app = Flask(__name__)
app.register_blueprint(views.bp)

if __name__ == '__main__':
	app.run(debug=True)
