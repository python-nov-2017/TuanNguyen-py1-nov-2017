from flask import Flask, session, render_template, request, redirect,url_for
import random, string
app = Flask(__name__)
key = ''.join(random.choice(string.lowercase) for i in range(10))
app.secret_key = key

def compare(num1, num2):
    session['color'] = "red";
    if num1 > num2:
        return "Too high!"        
    if num1 < num2:
        return "Too low!"
    if num1 == num2:
        session['color'] = "green"
        session['again'] = "show"
        session['start'] = 'none'
        return "{} was the number!".format(num1)

@app.route('/')
def index():
    if 'key' not in session:
        session['key'] = True
        session['random'] = random.randrange(0, 101)         
        session['display'] = "none"
        session['again'] = 'none'   
        session['start'] = 'show'     
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    try:
        session['guess'] = int(request.form['number'])
        session['message'] = compare(session['guess'],session['random'])
        session['display'] = "show"
    except:
        session['message'] = "That is not an number"
    print session['message']
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.pop("key")
    return redirect('/')

app.run(debug=True)