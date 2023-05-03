from flask import Flask, render_template

from mysql import connector

import Bdd

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def mainRoute():
    db = Bdd.Db()
    retour = db.getData()
    return render_template('main.html',
                           retour = retour)

@app.route('/login', methods = ['GET', 'POST'])
def loginRoute():
    return ''

@app.route('/logout', methods = ['GET'])
def logoutRoute():
    return ''

@app.route('/signup', methods = ['GET', 'POST'])
def signupRoute():
    return ''