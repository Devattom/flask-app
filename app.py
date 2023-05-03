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
    return render_template('main.html',
                           title = "SignUp",
                           path = path)