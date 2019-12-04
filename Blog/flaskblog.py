from flask import Flask, render_template, url_for, flash, redirect
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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
