from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from expovision.models import User
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired(message="Это поле не может быть пустым!"), Length(min=2, max=20, message="Длина")])
    name = StringField("Имя и фамилия", validators=[DataRequired(message="Это поле не может быть пустым!"), Length(min=2, max=40, message="Длина")])
    phone = StringField("Имя и фамилия", validators=[DataRequired(message="Это поле не может быть пустым!"), Length(min=11, max=12, message="Длина")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    confirm_password = PasswordField("Потверждение пароля", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Зарегистрироваться")