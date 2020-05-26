from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/forgotPass.html')
def forgotPass():
    return render_template('forgotPass.html')

@app.route('/quests.html')
def quests():
    return render_template('quests.html')






if __name__ == "__main__":
    app.run(debug=True)