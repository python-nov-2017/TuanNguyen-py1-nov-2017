from flask import Flask, session, render_template, request, redirect,url_for
import random, string
app = Flask(__name__)
key = ''.join(random.choice(string.lowercase) for i in range(10))
app.secret_key = key

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter']+=1
    print session['counter']
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter']+=1
    print session['counter']
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect('/')


app.run(debug=True)