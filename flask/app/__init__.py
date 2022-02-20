import json
import random
import logging
from functools import wraps

from flask import Flask, request, render_template, redirect
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from flask_bootstrap import Bootstrap
from app.model.models import User
from app.model.models import MonoalphabeticSubstitution
from app.model.models import CaesarEncryption
from app.model.models import EncryptedString
from flask_sqlalchemy import SQLAlchemy
from flask import session
import plotly
import plotly.express as px
import pandas as pd
from app.forms.forms import RegisterForm, LoginForm, EncryptionForm

db = SQLAlchemy()

app = Flask(__name__)
bootstrap = Bootstrap(app)
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
        form = LoginForm()
        if "user_name" in session:
            return func(*args, **kwargs)
        return render_template("login.html", form=form)
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
    form = RegisterForm()
    if request.method == "POST":
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        try:
            user = User(user_name, password)
            db.session.add(user)
            logger(f"User with user_name {user_name} created")
            db.session.commit()
            return redirect("/login")
        except IntegrityError:
            logger(f"user {user_name} already exists")
            error_message = "Usename already taken. Please try a different name"
            return render_template("register.html", form=form, error=error_message)
    return render_template("register.html", form=form)


@app.route("/account", methods=['GET'])
@requires_logged_in
def account():
    return render_template("account.html", user_name=session["user_name"])


@app.route("/login", methods=['GET', 'POST'])
@requires_not_logged_in
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_name = request.form["user_name"]
        password = request.form["password"]
        try:
            set_user(user_name)
            check_if_username_and_password_match(user_name, password)
        except NoResultFound:
            error_message = "Account name or password incorrect, please try again or register first"
            return render_template("login.html", error=error_message, form=form)
        session["user_name"] = request.form["user_name"]
        logger(f"session {session} started")
        return redirect("/encryption")
    return render_template("login.html", form=form)


def set_user(user_name: str):
    return db.session.query(User).filter_by(name=user_name).one()


def check_if_username_and_password_match(user_name: str, password: str):
    return db.session.query(User).filter_by(name=user_name, password=password).one()


@app.route("/logout")
@requires_logged_in
def logout():
    logout_user()
    return redirect("/login")


def logout_user():
    logger(f"ending session {session}")
    session.pop("user_name")


@app.route("/encryption", methods=['GET', 'POST'])
@requires_logged_in
def encryption():
    form = EncryptionForm()
    return render_template("encryption.html", user_name=session["user_name"], form=form)


@app.route("/result", methods=['GET', 'POST'])
@requires_logged_in
def result():
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
        logger(f"Added encrypted string {encrypted_string.content} with {encryption.type} encryption for user {user.name}")
    except KeyError as error:
        logger(f"error: {error}")
    except NoResultFound as error:
        logger(f"error: {error}")

    return encrypted_string.content



@app.route("/users")
@requires_logged_in
def users():
    all_users = db.session.query(User).all()
    return render_template("users.html", all_users=all_users)


@app.route("/statistics")
@requires_logged_in
def statistics():
    graph_json_user = get_strings_by_user()
    graph_json_chars = get_chars_count()
    return render_template("statistics.html", graph_json_user=graph_json_user, graph_json_chars=graph_json_chars)


def get_strings_by_user():
    strings_by_user = db.session.query(User.name, func.count(EncryptedString.id)).join(User).group_by(EncryptedString.user_id).all()
    strings_by_user_dict = {"Username": [], "Count": []}
    for user_name, count in strings_by_user:
        strings_by_user_dict.setdefault("Username").append(user_name)
        strings_by_user_dict.setdefault("Count").append(count)

    data_frame = pd.DataFrame.from_dict(strings_by_user_dict)
    fig = px.pie(data_frame, values="Count", names="Username", title="User share")
    fig.update_layout(title={"x": 0.5})
    graph_json_user = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json_user


def get_chars_count():
    strings_all = db.session.query(EncryptedString.content).all()
    first_tuple_elements = []
    for a_tuple in strings_all:
        first_tuple_elements.append(a_tuple[0])

    all_stings_in_one = ""
    for single_string in first_tuple_elements:
        all_stings_in_one = all_stings_in_one + single_string

    chars_count = pd.Series(list(all_stings_in_one), name="Count").value_counts().nlargest(n=15)
    data_frame = chars_count.to_frame().reset_index()
    data_frame.rename(columns={"index": "Chars"}, inplace=True)
    fig = px.bar(data_frame, x="Chars", y="Count", title="Character usage frequency (15 most used)")
    fig.update_layout(title={"x": 0.5})
    graph_json_chars = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graph_json_chars



