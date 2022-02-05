from wtforms import Form, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp


class RegisterForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password", [DataRequired(), Length(min=6, max=30)])


class LoginForm(Form):
    user_name = StringField("Username", [DataRequired(), Length(max=20)])
    password = PasswordField("Password", [DataRequired(), Length(max=30)])


class EncryptionForm(Form):
    shift = IntegerField("Shift (1-1024)", [NumberRange(min=1, max=1024, message="Invalid number")])
    user_input = StringField("Enter text", validators=[DataRequired(), Length(max=50), Regexp('^[A-Za-z0-9 r!#$%&\'()*+,-.|\/:;<=>?@[\]^_`{|}~\"]+$')])

