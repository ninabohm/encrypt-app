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
from flask import session

db = SQLAlchemy()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "Ph:3KN*T7eW=mBJ(2>D/FY!"
app.logger.setLevel(logging.INFO)
logger = app.logger.info
db.init_app(app)

with app.app_context():
    db.create_all()


def requires_logged_in(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "user_name" in session:
            return func(*args, **kwargs)
        return render_template("login.html")
    return wrapped_func


def requires_not_logged_in(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if "user_name" not in session:
            return func(*args, **kwargs)
        return redirect("/encryption")
    return wrapped_func


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
            logger(f"User with user_name {user_name} created")
            db.session.commit()
            return redirect("/login")
        except IntegrityError as error:
            logger(f"user {user_name} already exists")
            return render_template("register.html", error=error)
    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
@requires_not_logged_in
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
        logger(f"session {session} started")
        return redirect("/encryption")
    return render_template("login.html")


def set_user(user_name: str):
    try:
        return check_if_user_exists(user_name)
    except NoResultFound:
        logger(f"User with name {user_name} does not exist")


def check_if_user_exists(user_name: str):
    return db.session.query(User).filter_by(name=user_name).one()


def check_if_username_and_password_match(user_name: str, password: str):
    return db.session.query(User).filter_by(name=user_name, password=password).one()


@app.route("/logout")
@requires_logged_in
def logout():
    if "user_name" in session:
        logout_user()
        return redirect("/")
    return redirect("/login")


def logout_user():
    logger(f"ending session {session}")
    session.pop("user_name")


@app.route("/encryption", methods=['GET', 'POST'])
@requires_logged_in
def encryption():
    return render_template("encryption.html", user_name=session["user_name"])


@app.route("/result", methods=['GET', 'POST'])
@requires_logged_in
def result():
    encryption_base = request.form.get("encryption_base")
    user_input = request.form.get("user_input")
    try:
        shift = int(request.form.get("shift"))
    except ValueError:
        shift = random.randint(0, 1024)
    except TypeError as error:
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
        logger(f"Added encrypted string {encrypted_string.content} with {encryption.type} encryption for user {user.name}")
    except KeyError as error:
        logger(f"error: {error}")

    return render_template(
        "result.html",
        encryption_base=encryption_base,
        shift=shift,
        user_input=user_input,
        encrypted_string=encrypted_string.content
    )


@app.route("/users")
@requires_logged_in
def users():
    if "user_name" in session:
        all_users = db.session.query(User).all()
        return render_template("users.html", all_users=all_users)
    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True)
