from App import app
from flask import render_template, url_for


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/singup')
def signup():
    return render_template('signup.html')

@app.route('/forgotPass')
def forgotPass():
    return render_template('forgotPass.html')

@app.route('/quests')
def quests():
    return render_template('quests.html')

