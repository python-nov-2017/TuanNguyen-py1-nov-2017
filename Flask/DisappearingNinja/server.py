from flask import Flask, render_template, request, flash, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
@app.route('/ninja/<char>')
def ninja(char=None):
    return render_template('ninja.html',name=char)

app.run(debug=True)