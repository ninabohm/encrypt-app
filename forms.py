from wtforms import Form, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class RegisterForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password (min. 6)", [DataRequired(), Length(min=6, max=30)])


class LoginForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password", [DataRequired(), Length(min=6, max=30)])


class EncryptionForm(Form):
    shift = IntegerField("Shift (1-1024)", [NumberRange(min=1, max=1024, message="Invalid number")])
    user_input = StringField("Your text to be encrypted", [DataRequired(), Length(max=50)])

