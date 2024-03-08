from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule('/shorten_url', view_func=views.shorten_url, methods=['POST'])
app.add_url_rule('/<string:short_url>', view_func=views.redirect_url, methods=['GET'])
app.add_url_rule('/analytics/<string:short_url>', view_func=views.get_analytics, methods=['GET'])

if __name__ == '__main__':
	app.run(debug=True)

