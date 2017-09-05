from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
	first_name = StringField('first_name', validators=[DataRequired()])
	username = StringField('Username: ', validators=[DataRequired()])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm', message='Passwords must match')
		])
	confirm = PasswordField('Repeat Password')