from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	email = StringField("email", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])

class PostForm(FlaskForm):
	tittle = StringField("tittle", validators=[DataRequired()])
	content = TextAreaField("content", validators=[DataRequired(), validators.length(max=1000)])