from flask import Flask, render_template, request, flash, redirect, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    error = False
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty!")
        error = True
    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
        error = True
    elif len(request.form['comment']) > 120:
        flash("Comment field cannot exceed 120 charaters!")
        error = True
    if error:        
        return redirect('/')    
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template('result.html', name=name, location=location, language=language, comment=comment)
app.run(debug=True)