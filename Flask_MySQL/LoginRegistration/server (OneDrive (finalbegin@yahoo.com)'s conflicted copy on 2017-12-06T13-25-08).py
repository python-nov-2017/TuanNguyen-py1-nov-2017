from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

# GET	'/'	index()	Display all of the friends on the index.html page
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', all_friends=friends)

# POST	'/friends'	create()	Handle the add friend form submit and create the friend in the DB
@app.route('/friends', methods=['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['email']
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'], 
        'last_name':  request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)    
    return redirect('/')

# GET	'/friends/<id>/edit'	edit(id)	Display the edit friend page for the particular friend
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', friends=friends)

# POST '/friends/<id>'	update(id)	Handle the edit friend form submit and update the friend in the DB
@app.route('/friends/<id>', methods=['POST'])
def updated(id):
    print request.form['first_name']
    print request.form['last_name']
    print request.form['email']
    query = "UPDATE friends \
            SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() \
            WHERE id = :id"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'email': request.form['email'],
        "id": id
    }    
    mysql.query_db(query, data)       
    return redirect('/')

# POST	'/friends/<id>/delete'	destroy(id)	Delete the friend from the DB
@app.route('/friends/<id>/delete')
def destroyed(id):
    query = "DELETE FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)