from flask import Flask, render_template, url_for, redirect
from form import RegistrationForm, LogInForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ad25d20e352714fa4fbbc04f13a0f043'

posts = [
    {
        'author': 'Sayan Ghosh',
        'title': 'my 1st blog',
        'content': 'my 1st content',
        'date': '24nov,2019'
    },
{
        'author': 'Rimo',
        'title': 'my 2nd blog',
        'content': 'my 2nd content',
        'date': '25nov,2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods = ['POST','GET'])
def login():
    form = LogInForm()
    return render_template('login.html', title = 'LogIn', form=form)


if (__name__) == '__main__':
    app.run(debug = True)
