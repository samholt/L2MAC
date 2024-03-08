from flask import Flask

app = Flask(__name__)
app.config['DATABASE'] = {}

@app.route('/')
def home():
	return 'Hello, World!'

if __name__ == '__main__':
	app.run(debug=True)
