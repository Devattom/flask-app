from flask import Flask, render_template, request, redirect, url_for
import bcrypt
from mysql import connector
import re
from datetime import date

import Bdd

user_list = []

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def mainRoute():
    path = request.path
    today = date.today()
    year = today.year
    if user_list:
        message = "Bonjour " + user_list[0]
    else:
        message = "Bonjour utilisateur anonyme"
    return render_template('main.html',
                           title = "Home",
                           path = path,
                           current_year = year,
                           user_list = user_list,
                           message = message,
                          )

@app.route('/login', methods = ['GET', 'POST'])
def loginRoute():
    path = request.path
    today = date.today()
    year = today.year
    # test de la method et récupération des données
    if request.method == 'POST':
        input_email = request.form['email']
        input_password = request.form['password']
        db = Bdd.Db()
        data = db.getUserByEmail(input_email)
        error = ''
        if data:
            db_password = data[1]
            #check mdp via methode de bcrypt
            if bcrypt.checkpw(input_password.encode('utf-8'), db_password.encode('utf-8')):
                user_list.append(data[0])
            else:
                error = "L'identifiant ou le mot de passe est incorrect"
        else:
            error = "L'identifiant ou le mot de passe est incorrect"
        return render_template('main.html',
                           title = 'Login',
                           path = path,
                           current_year = year,
                           data = data,
                           error = error,
                           user_list = user_list)
    else: 
        return render_template('main.html',
                        title = 'Login',
                        path = path,
                        current_year = year)




@app.route('/logout', methods = ['GET'])
def logoutRoute():
    user_list.clear()
    return redirect(url_for('mainRoute'))

@app.route('/signup', methods = ['GET', 'POST'])
def signupRoute():
    path = request.path
    today = date.today()
    year = today.year
    # test de la method et récupération des données
    if request.method == 'POST':
        user_name = request.form['name']
        user_firstname = request.form['firstname']
        user_email = request.form['mail']
        psw1 = request.form['psw1']
        psw2 = request.form['psw2']
        message = {}
        # regex pour validation des données
        regex_mail = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,4}'
        regex_names = '[a-zA-Z-]+'
        
        if not re.fullmatch(regex_mail, user_email) or user_email == None:
            message['email'] = "Veuillez rentrer un email au format valide"
            email = False
        else:
            email = True
        if not re.fullmatch(regex_names, user_name) or user_name == None:
            message['name'] = "Veuillez rentrer un nom valide"
            name = False
        else:
            name = True
        if not re.fullmatch(regex_names, user_firstname) or user_firstname == None:
            message['firstname'] = "Veuillez rentrer un prénom valide"
            firstname = False
        else:
            firstname = True

        #si tout les champs sont correctement rempli et que les mdp correspondent, alors enregistrement dans la bdd
        if email and name and firstname and psw1:
            if psw1 == psw2:
                db = Bdd.Db()
                if db.getUserByEmail(user_email):
                    message['user'] = "Un compte existe déjà avec cet Email"
                else:
                    #hashage mdp via bcrypt
                    salt = bcrypt.gensalt(rounds = 15)
                    crypt_psw = bcrypt.hashpw(psw1.encode('utf-8'), salt)
                    db.insertUser(user_name, user_firstname, user_email, crypt_psw)
                    message = {}
                    message['success'] = "Vous êtes bien inscrit, vous pouvez maintenant vous connecter"
            else:
                message['password'] = 'Veuillez Saisir deux mots de passe identiques'

            
        return render_template('main.html',
                           title = "SignUp",
                           path = path,
                           current_year = year,
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
                               path=path,
                               current_year = year)

@app.errorhandler(404)
def route404(erreur):
    today = date.today()
    year = today.year
    erreur_404 = True
    return render_template('main.html',
                           code = 404,
                           title = 'Erreur 404',
                           erreur_404 = erreur_404,
                           current_year = year)
