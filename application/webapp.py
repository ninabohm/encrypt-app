import random
import logging
from flask import Flask, request, render_template
from sqlalchemy.orm.exc import NoResultFound
from modelsFlask import User
from modelsFlask import db


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db.init_app(app)

with app.app_context():
    db.create_all()

logger = logging.getLogger(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get("user")
        try:
            # TODO: check if user exists
            user = db.session.query(User).filter_by(name=user_name).first()
            print(user)
            return user
        except NoResultFound:
            user = User(user_name)
            db.session.add(user)
            db.session.commit()
    return render_template("index.html")


@app.route("/encryption", methods=['GET', 'POST'])
def encryption():
    user_name = request.form.get("user")
    user_curr = User(user_name)
    db.session.add(user_curr)
    return render_template(
        "encryption.html",
        user=user_name
    )


@app.route("/result", methods=['POST'])
def result():
    encryption_base = request.form.get("encryption_base")
    user_input = request.form.get("user_input")
    shift = int(request.form.get("shift"))
    user = User("testuser")

    if encryption_base == "caesar":
        encryption = CaesarEncryption()
        ##shift = encryption.get_shift_value()
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
        shift = 0

    encryption_content = encryption.encrypt_input(user_input, shift)
    encrypted_string = EncryptedString(encryption_content, encryption, user).content

    return render_template(
        "result.html",
        encryption_base=encryption_base,
        shift=shift,
        user_input=user_input,
        encrypted_string=encrypted_string
    )


if __name__ == '__main__':
    app.run(debug=True)
