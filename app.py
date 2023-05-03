from flask import Flask, render_template, request

from mysql import connector

import Bdd



app = Flask(__name__)

@app.route("/", methods = ['GET'])
def mainRoute():
    path = request.path
    db = Bdd.Db()
    retour = db.getData()
    return render_template('main.html',
                           title = "Home",
                           path = path)

@app.route('/login', methods = ['GET', 'POST'])
def loginRoute():
    return ''

@app.route('/logout', methods = ['GET'])
def logoutRoute():
    return ''

@app.route('/signup', methods = ['GET', 'POST'])
def signupRoute():
    path = request.path
    
    if request.method == 'POST':
        user_name = request.form['name']
        user_firstname = request.form['firstname']
        user_email = request.form['mail']
        psw1 = request.form['psw1']
        psw2 = request.form['psw2']
        return render_template('main.html',
                           title = "SignUp",
                           path = path,
                           name = user_name,
                           firstname = user_firstname,
                           email = user_email,
                           psw1 = psw1,
                           psw2 = psw2)
    else:
        return render_template('main.html',
                               title = "SignUp",
                               path=path)