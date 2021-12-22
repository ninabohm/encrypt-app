from flask import Flask, request, render_template
from model.models import EncryptedString
from model.models import CaesarEncryption
from model.models import MonoalphabeticSubstitution
from model.models import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encryption", methods=['GET'])
def encryption():
    return render_template("encryption.html")


@app.route("/result", methods=['POST'])
def result():
    encryption_base = request.form.get("encryption_base")
    user_input = request.form.get("user_input")
    shift = int(request.form.get("shift"))
    user = User("testuser")

    if encryption_base == "caesar":
        encryption = CaesarEncryption()
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
