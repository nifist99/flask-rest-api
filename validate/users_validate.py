from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    password        = PasswordField("password", validators=[DataRequired()])
    name            = StringField("name")
    email           = StringField("email", validators=[DataRequired()])