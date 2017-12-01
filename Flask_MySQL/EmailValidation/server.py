from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'emailsdb')
@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('index.html', all_emails=emails)

@app.route('/emails', methods=['POST'])
def create():
    print request.form['email']
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    query = "INSERT INTO emails (address, created_at, updated_at) VALUES (:address, NOW(), NOW())"
    data = {
             'address': request.form['email']
           }
    mysql.query_db(query, data)    
    return redirect('/success')

@app.route('/success')
def sucess():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template("success.html", all_emails=emails)



# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])
# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends \
#              SET first_name = :first_name, last_name = :last_name, occupation = :occupation \
#              WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')
app.run(debug=True)