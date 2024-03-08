from flask import Flask, render_template, request, redirect, url_for, flash
from gcs_main import main

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        main()
        flash('GCS application executed successfully', 'success')
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)