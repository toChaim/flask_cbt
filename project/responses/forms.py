from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired

class ResponseForm(FlaskForm):
	title = StringField('Thought title: ', validators=[DataRequired()])
	# affirmation = BooleanField('Positive: ')
	affirmation = RadioField('Is it positive? ', choices=[('True','Positive'), ('', 'Neutral'), ('False','Negative')])

class ResponseDeleteForm(FlaskForm):
	pass
