from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'KeepItSecretKeepItSafe'

mysql = MySQLConnector(app,'logindb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    error = False
    email = request.form['email']
    password = request.form['password']
    if any(len(request.form[key]) < 1 for key in request.form):
        error = True
        flash("All fields must be filled!")                 
    if len(email)<= 0 or len(password)<=0:
        flash("Email and Password field cannot be empty.")
    if (len(request.form['password']) < 8):
        error = True
        flash("Password field must be more than 8 letters.") 
     

    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': email }
    users = mysql.query_db(query, data)
    if bcrypt.check_password_hash(users[0]['password'], password):
        return render_template('success.html', all_users=users)
    else:
        error = True
        flash("Wrong password.")
    if error:
        return redirect('/')     


@app.route('/registration', methods=['POST'])
def create():
    error = False   
    if (len(request.form['first_name']) < 2):
        error = True
        flash("First name field must be more than 2 letters.")
    if not request.form['first_name'].isalpha():
        error = True
        flash("First name field must contain no number.")
    if (len(request.form['last_name']) < 2):
        error = True
        flash("Last name field must be more than 2 letters.")
    if not request.form['last_name'].isalpha():
        error = True
        flash("Last name field must contain no number.")     
    if not EMAIL_REGEX.match(request.form['email']):
        error = True
        flash("Invalid Email Address!")
    if (len(request.form['password']) < 8):
        error = True
        flash("Password field must be more than 8 letters.") 
    if not (request.form['password'] == request.form['pwd_confirm']):
        error = True
        flash("Password Confirmation do not match.")
    if error:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'], 
        'last_name':  request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    mysql.query_db(query, data)    
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': request.form['email'] }
    users = mysql.query_db(query, data)
    return render_template('success.html', all_users = users)


app.run(debug=True)