from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
import re, random, string
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = ''.join(random.choice(string.lowercase) for i in range(10))

mysql = MySQLConnector(app,'forumdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    if 'userid' in session:
        return redirect('/wall')
    return render_template('index.html')

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
    return redirect("/wall")

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
        if 'userid' not in session:
            session['userid'] = users[0]['id']
            return redirect('/wall')
    else:
        error = True
        flash("Wrong password.")
    if error:
        return redirect('/')     

@app.route('/logoff')
def logoff():
    session.pop('userid')
    return redirect('/')

@app.route('/wall')
def wall():
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': session['userid']}
    user = mysql.query_db(query, data)[0]

    query = 'SELECT users.id as user_id, messages.id as message_id, concat_ws(" ", users.first_name, users.last_name) as name, messages.message, date_format(messages.created_at,"%M %D %Y" ) as created_at \
             FROM users \
             LEFT JOIN messages \
             ON users.id = messages.user_id \
             ORDER BY messages.created_at DESC'
    messages = mysql.query_db(query)

    query = 'SELECT users.id as user_id, messages.id as message_id, comments.id as comment_id, concat_ws(" ", users.first_name, users.last_name) as name, comments.comment, date_format(comments.created_at,"%M %D %Y" ) as created_at\
             FROM comments \
             LEFT JOIN users \
             ON comments.user_id = users.id \
             LEFT JOIN messages \
             ON comments.message_id = messages.id \
             ORDER BY comments.created_at'
    comments = mysql.query_db(query)

    return render_template("wall.html", user=user, all_messages=messages, all_comments=comments)
    
@app.route('/post', methods=['POST'])
def posting():
    message = request.form["message"]
    query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :user_id)"
    data = {
        'message': message,
        'user_id': session['userid']
    }
    mysql.query_db(query,data)
    return redirect ('/wall')

@app.route('/comment', methods=['POST'])
def comment():
    comment = request.form["comment"]
    message_id = request.form["message_id"]
    print message_id
    query = "INSERT INTO comments (comment, created_at, updated_at, message_id, user_id) VALUES (:comment, NOW(), NOW(), :message_id, :user_id)"
    data = {
        'comment': comment,
        'user_id': session['userid'],
        'message_id': message_id
    }
    mysql.query_db(query,data)
    return redirect ('/wall')    

@app.route('/delete', methods=['POST'])
def delete():
    message_id = request.form['message_id']
    print message_id
    query = "DELETE FROM messages WHERE id = :message_id"
    data = { "message_id": message_id}
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)