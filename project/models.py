from project import bcrypt, db, login_manager
from flask_login import UserMixin

MatchResponse = db.Table('match_responses',
	db.Column('id', db.Integer, primary_key=True),
	db.Column('match_id', db.Integer, db.ForeignKey('matches.id', ondelete='cascade')),
	db.Column('response_id', db.Integer, db.ForeignKey('responses.id', ondelete='cascade'))
	)

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text, nullable=False)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	prompts = db.relationship('Prompt', backref='user')

	def __init__(self, first_name, username, password):
		self.first_name = first_name
		self.username = username
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Prompt(db.Model):
	__tablename__ = 'prompts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	affirmation = db.Column(db.Boolean)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'), nullable=False)
	__table_args__ = (db.UniqueConstraint('user_id', 'title', name='_user_titel_uc'),)
	responses = db.relationship('Resonse', backref='prompt')

	def __init__(self, title, affirmation, user_id):
		self.title = title
		self.affirmation = affirmation
		self.user_id = user_id

class Response(db.Model):
	__tablename__ = 'responses'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=False)
	affirmation = db.Column(db.Boolean)
	prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id', ondelete='cascade'), nullable=False)
	__table_args__ = (db.UniqueConstraint('prompt_id', 'title', name='_prompt_titel_uc'),)

	def __init__(self, title, affirmation, user_id):
		self.title = title
		self.affirmation = affirmation
		self.user_id = user_id

class Match(db.Model):
	__tablename__ = 'matches'

	id = db.Column(db.Integer, primary_key=True)
	prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id'), nullable=False)
	pick_id = db.Column(db.Integer, db.ForeignKey('responses.id'))
	start_time = db.Column(db.DateTime)
	end_time = db.Column(db.DateTime)

