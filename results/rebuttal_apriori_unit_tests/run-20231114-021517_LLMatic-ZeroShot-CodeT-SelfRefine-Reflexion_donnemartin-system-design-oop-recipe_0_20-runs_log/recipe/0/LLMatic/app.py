from flask import Flask

app = Flask(__name__)
app.secret_key = 'super secret key'

import views
