from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def mainRoute():
    return 'hello world'

@app.route('/login', methods = ['GET', 'POST'])
def loginRoute():
    return ''

@app.route('/logout', methods = ['GET'])
def logoutRoute():
    return ''

@app.route('/signup', methods = ['GET', 'POST'])
def signupRoute():
    return ''