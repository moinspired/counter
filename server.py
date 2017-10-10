from flask import Flask, render_template, request, redirect, session
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:

        session['count'] = 1
    return render_template('index.html')

app.run(debug=True)
