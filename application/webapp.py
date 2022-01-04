import random
import logging
from flask import Flask, request, render_template
from sqlalchemy.orm.exc import NoResultFound
from modelsFlask import User
from modelsFlask import MonoalphabeticSubstitution
from modelsFlask import CaesarEncryption
from modelsFlask import EncryptedString
from modelsFlask import db


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///webdata.db"
db.init_app(app)

with app.app_context():
    db.create_all()

logger = logging.getLogger(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/encryption", methods=['GET', 'POST'])
def encryption():
    user_name = request.form.get("user")
    try:
        check_if_user_exists(user_name)
        user = db.session.query(User).filter_by(name=user_name).first()
        logger.info(f"Login for user {user_name} successful")
        return user
    except NoResultFound:
        logger.info(f"User with name {user_name} does not exist yet, creating user on the fly")
        user = User(user_name)
        db.session.add(user)
        db.session.commit()
        return user
    finally:
        return render_template("encryption.html", user=user_name)


def check_if_user_exists(user_name: str):
    return db.session.query(User).filter_by(name=user_name).one()


@app.route("/result", methods=['POST'])
def result():
    encryption_base = request.form.get("encryption_base")
    user_input = request.form.get("user_input")
    shift = int(request.form.get("shift"))
    user = User("testuser")

    if encryption_base == "caesar":
        encryption = CaesarEncryption()
        db.session.add(encryption)
        #shift = encryption.get_shift_value()
        shift = request.form.get["shift"]
        if shift == "":
            shift_value = random.randint(0, 1024)
            logger.info(f"User chose shift of {shift_value} ")
        else:
            try:
                shift_value = int(shift)
                logger.info(f"User chose shift of {shift_value}")
                return shift_value
            except ValueError:
                shift_value = int(shift_value)
                logger.info(f"User chose shift of {shift_value}")
                return shift_value
    else:
        encryption = MonoalphabeticSubstitution()
        db.session.add(encryption)
        shift = 0

    encryption_content = encryption.encrypt_input(user_input, shift)
    encrypted_string = EncryptedString(encryption_content, encryption, user).content
    try:
        #db.session.add(encrypted_string)
        db.session.commit()
    except KeyError as error:
        logger.info(f"error: {error}")


    return render_template(
        "result.html",
        encryption_base=encryption_base,
        shift=shift,
        user_input=user_input,
        encrypted_string=encrypted_string
    )


if __name__ == '__main__':
    app.run(debug=True)
