from flask import Flask, redirect, request,  render_template, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def index():
    if 'key' not in session:
        session['key'] = True
        session['current_gold'] = 0
        session['record'] = []
    print session['current_gold']
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process():
    if request.form['building'] == 'farm':
        amount = random.randrange(10, 20)    
    elif request.form['building'] == 'cave':
        amount = random.randrange(5, 10) 
    elif request.form['building'] == 'house':
        amount = random.randrange(2, 5) 
    elif request.form['building'] == 'casino':
        amount = random.randrange(-50, 50)
    print amount     
    session['current_gold']+=amount
    now = datetime.datetime.now()
    time = now.strftime("%Y/%m/%d %I:%M %p")
    
    data = {
        'place': request.form['building'],
        'gold': amount,
        'time': time,
        'color': 'red'
    }    
    session['record'].insert(0,data)
    print session['record']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('key')
    return redirect('/')


app.run(debug=True)