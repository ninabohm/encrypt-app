import random
import logging

from flask import Flask, request, render_template
from sqlalchemy.orm.exc import NoResultFound
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


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["user_name"] = request.form["user_name"]
    return render_template("login.html")


@app.route("/encryption", methods=['GET', 'POST'])
def encryption():
    user_name = request.form.get("user_name")
    get_user(user_name)
    return render_template("encryption.html", user_name=user_name)


def get_user(user_name: str):
    try:
        check_if_user_exists(user_name)
        user = db.session.query(User).filter_by(name=user_name).first()
    except NoResultFound:
        print("throwing exception!")
        app.logger.info(f"User with name {user_name} does not exist yet, creating user on the fly")
        user = User(user_name)
        db.session.add(user)
        db.session.commit()
    return user


def check_if_user_exists(user_name: str):
    return db.session.query(User).filter_by(name=user_name).one()


@app.route("/result", methods=['POST'])
def result():
    encryption_base = request.form.get("encryption_base")
    user_input = request.form.get("user_input")
    try:
        shift = int(request.form.get("shift"))
    except ValueError:
        shift = random.randint(0, 1024)
    user_name = request.form.get("user_name")
    user = get_user(user_name)

    if encryption_base == "caesar":
        encryption = CaesarEncryption()
    else:
        encryption = MonoalphabeticSubstitution()
        shift = 0

    encryption_content = encryption.encrypt_input(user_input, shift)
    db.session.add(encryption)
    try:
        encrypted_string = EncryptedString(encryption_content, encryption, user)
        db.session.add(encrypted_string)
        db.session.commit()
    except KeyError as error:
        app.logger.info(f"error: {error}")

    return render_template(
        "result.html",
        encryption_base=encryption_base,
        shift=shift,
        user_input=user_input,
        encrypted_string=encrypted_string.content
    )


if __name__ == '__main__':
    app.run(debug=True)
