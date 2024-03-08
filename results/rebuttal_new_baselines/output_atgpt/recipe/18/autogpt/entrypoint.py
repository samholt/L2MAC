# Import necessary modules
import os
import flask
from flask import Flask, request

# Initialize Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Recipe Sharing Platform!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))