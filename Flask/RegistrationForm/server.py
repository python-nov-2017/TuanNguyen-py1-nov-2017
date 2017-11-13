from flask import Flask, render_template, request, flash, redirect, session, url_for
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    error = False
    print request.form
    if any(len(request.form[key]) < 1 for key in request.form):
        error = True
        flash("All fields must be filled!")     
    if not (request.form['fname']+request.form['lname']).isalpha():
        error = True
        flash("Names cannot contain numbers!")
    if len(request.form['pword']) < 8:
        error = True
        flash("Password has to be more than 8 characters!")
    if not EMAIL_REGEX.match(request.form['email']):
        error = True
        flash("Invalid Email Address!")
    if request.form['pword'] != request.form['pword_confirm']:
        error = True
        flash("Password Confirmation is not matched!")
    print request.form['pword']
    if not any(char.isupper() for char in request.form['pword']) or not any(char.isdigit() for char in request.form['pword']):
        error = True
        flash("Password has to have at least one Uppercase letter and one Number!!")
    if error:        
        return redirect('/')    
    flash("Thanks for submitting your information.")
    return redirect('/')
app.run(debug=True)