from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators
from wtforms.validators import DataRequired

class PromptForm(FlaskForm):
	title = StringField('Thought title: ', validators=[DataRequired()])
	affirmation = BooleanField('Positive: ')