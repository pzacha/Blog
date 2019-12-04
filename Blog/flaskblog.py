from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "9c6db76cf0d55cc5dcfcd4d183aad50d"

posts = [
    {
        "author": "Piotr Zacha",
        "title": "Post 1",
        "content": "Content 1",
        "date": "02.12.2019",
    },
    {
        "author": "Jake Doe",
        "title": "Post 2",
        "content": "Content 2",
        "date": "03.12.2019",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form = form)

if __name__ == "__main__":
    app.run(debug=True)
