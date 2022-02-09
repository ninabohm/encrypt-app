from wtforms import Form, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp, ValidationError


class RegisterForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password", [DataRequired(), Length(min=6, max=30)])


class LoginForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password", [DataRequired(), Length(max=30)])


class EncryptionForm(Form):
    shift = IntegerField("Shift (1-1024)", [NumberRange(min=1, max=1024, message="Invalid number")])
    user_input = StringField("Enter text", [DataRequired(), Length(max=50)])



# '^[A-Za-z0-9 r!#$%&\'()*+,-.|\/:;<=>?@[\]^_`{|}~\"]+$'