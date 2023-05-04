from flask import Flask, render_template, request
import bcrypt
from mysql import connector
import re

import Bdd



app = Flask(__name__)

@app.route("/", methods = ['GET'])
def mainRoute():
    path = request.path
    db = Bdd.Db()
    retour = db.getData()
    return render_template('main.html',
                           title = "Home",
                           path = path,
                           retour = retour)

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
        message = {}

        regex_mail = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,4}'
        regex_names = '[A-za-z._%-]'
    
        if not re.fullmatch(regex_mail, user_email):
            message['email'] = "Veuillez rentrer un email au format valide"
        if not re.fullmatch(regex_names, user_name):
            message['name'] = "Veuillez rentrer un nom valide"
        if not re.fullmatch(regex_names, user_firstname):
            message['firstname'] = "Veuillez rentrer un prénom valide"

        if psw1 and psw1 == psw2:
            db = Bdd.Db()
            if db.getUserByEmail(user_email):
                message['user'] = "Un compte existe déjà avec cet Email"
            else:
                salt = bcrypt.gensalt(rounds = 15)
                crypt_psw = bcrypt.hashpw(psw1.encode('utf-8'), salt)
                db.insertUser(user_name, user_firstname, user_email, crypt_psw)
        else:
            message['password'] = 'Veuillez Saisir deux mots de passe identiques'

            
        return render_template('main.html',
                           title = "SignUp",
                           path = path,
                           name = user_name,
                           firstname = user_firstname,
                           email = user_email,
                           psw1 = psw1,
                           psw2 = psw2,
                           message = message,
                           )
    else:
        return render_template('main.html',
                               title = "SignUp",
                               path=path)