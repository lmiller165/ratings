"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template("homepage.html")


@app.route("/users")
def user_list(): 
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)



@app.route("/registration", methods=["GET"])
def registration_view():
    return render_template("registration_form.html")


@app.route("/registration", methods=["POST"])
def registration_process():
    """Check if user is part of our database, if not, add them"""

    #if email in users, redirect to log in page
    email = request.form.get("email")
    password = request.form.get("password")

    if email == User.query.filter_by(email=email):
        return redirect("/log_in")

    #else add email and password to database 
    else:
        user = User(email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect("/users")


@app.route("/login", methods=["GET"])
def login():
    """Show log in page"""
    return render_template("log_in.html")


@app.route("/login", methods=["POST"])
def login():
    """Show log in page"""

    email = request.form.get("email")
    password = request.form.get("password")

    if (email == User.query.filter_by(email=email)
        and password == #writequery) 


        email & password == password


    return render_template("log_in.html")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')


