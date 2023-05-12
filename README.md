# flask-app
Little Flask app which handle user identification throught a database to store the user. It use Flask, bcrypt for the encryption of the password and some native python module.
This app allow signup, signin et logout and show different things depends of the status of the user.

## Init
If you are using Vs Code first create the virtual environment:
* Ctrl+shift+P
* Pyhton create environment
* Then choose VENV and the folder where your cloned this project.
* Choose your interpreter

If you want to do it with command line :

(Windows)
```console
$ mkdir myproject
$ cd myproject
$ py -3 -m .venv venv
```
(Linux/Mac)
```console
$ mkdir myproject
$ cd myproject
$ python3 -m .venv venv
```

In any case you have to activate the scripts at the end :
(Windows)
```console
$ .venv\Scripts\activate
```
(Linux/Mac)
```console
$ .venv\bin\activate
```

## Install Flask
Once you have set the virtual environment you have to download and install Flask:
```console
$ pip install Flask
```
## Install MySql
Don't forget to install Mysql connector for the database connection :

```console
$ pip install mysql-connector-python
```
## Run app

Once everything is set you should normally be able to work on this project, for run the app just do :

```console
$ flask run
```

Enjoy !

###Comments
Don't hesitate to tell me if you see something that can be improved, I am a begginer and deeply into sharing and learning. 
