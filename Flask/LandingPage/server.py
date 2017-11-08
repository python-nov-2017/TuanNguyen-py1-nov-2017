from flask import Flask, render_template, request

app = Flask(__name__)

print app

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return "Ninja information is here"

@app.route('/ninjas/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/ninjas/dojos/process', methods=["POST"])
def process():
    str = "First name: " + request.form["first_name"]    
    str += "Last name: " + request.form["last_name"]
    str += "Email: " + request.form["email"]
    return str

app.run(debug=True)