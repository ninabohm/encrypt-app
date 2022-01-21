import random
import logging
from functools import wraps

from flask import Flask, request, render_template, redirect
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from models import User
from models import MonoalphabeticSubstitution
from models import CaesarEncryption
from models import EncryptedString
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import session

db = SQLAlchemy()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "Ph:3KN*T7eW=mBJ(2>D/FY!"
app.logger.setLevel(logging.INFO)
db.init_app(app)

with app.app_context():
    db.create_all()


def requires_login(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        else:
            return redirect("/login")

    return wrapped_func


@app.route("/test")
def test():
    if "user_name" in session:
        return "test"
    return redirect("/login")


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        try:
            user = User(user_name, password)
            db.session.add(user)
            app.logger.info(f"User with user_name {user_name} created")
            db.session.commit()
            return redirect("/login")
        except IntegrityError as error:
            app.logger.info(f"user {user_name} already exists")
            return render_template("register.html", error=error)
    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        password = request.form["password"]
        try:
            check_if_user_exists(user_name)
            check_if_username_and_password_match(user_name, password)
        except NoResultFound as error:
            return render_template("login.html", error=error)
        session["user_name"] = request.form["user_name"]
        app.logger.info(f"session {session} started")
        return redirect("/encryption")
    return render_template("login.html")


def set_user(user_name: str):
    try:
        check_if_user_exists(user_name)
        user = db.session.query(User).filter_by(name=user_name).first()
        return user
    except NoResultFound:
        app.logger.info(f"User with name {user_name} does not exist")


def check_if_user_exists(user_name: str):
    return db.session.query(User).filter_by(name=user_name).one()


def check_if_username_and_password_match(user_name: str, password: str):
    matching = db.session.query(User).filter_by(name=user_name, password=password).one()
    app.logger.info(matching)
    return matching


@app.route("/logout")
def logout():
    if "user_name" in session:
        logout_user()
        return redirect("/")
    return redirect("/login")


def logout_user():
    app.logger.info(f"ending session {session}")
    session.pop("user_name")


@requires_login
@app.route("/encryption", methods=['GET', 'POST'])
def encryption():
    try:
        return render_template("encryption.html", user_name=session["user_name"])
    except KeyError as error:
        app.logger.info(error)
        return redirect("/login")


@requires_login
@app.route("/result", methods=['GET', 'POST'])
def result():
    if "user_name" in session:
        encryption_base = request.form.get("encryption_base")
        user_input = request.form.get("user_input")
        try:
            shift = int(request.form.get("shift"))
        except ValueError:
            shift = random.randint(0, 1024)
        except TypeError:
            return redirect("/encryption")

        if encryption_base == "caesar":
            encryption = CaesarEncryption()
        else:
            encryption = MonoalphabeticSubstitution()
            shift = 0

        encryption_content = encryption.encrypt_input(user_input, shift)
        db.session.add(encryption)
        try:
            user = set_user(session["user_name"])
            encrypted_string = EncryptedString(encryption_content, encryption, user)
            db.session.add(encrypted_string)
            db.session.commit()
            app.logger.info(f"Added encrypted string {encrypted_string.content} with {encryption.type} encryption for user {user.name}")
        except KeyError as error:
            app.logger.info(f"error: {error}")

        return render_template(
            "result.html",
            encryption_base=encryption_base,
            shift=shift,
            user_input=user_input,
            encrypted_string=encrypted_string.content
        )
    else:
        return redirect("/login")


@app.route("/users")
def users():
    all_users = db.session.query(User).all()
    return render_template("users.html", all_users=all_users)


if __name__ == '__main__':
    app.run(debug=True)
