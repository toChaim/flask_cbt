from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.decorators import ensure_correct_user
from project.models import Match
from project.matches.forms import MatchForm
from project import db
from sqlalchemy.exc import IntegrityError

matches_blueprint = Blueprint('matches', __name__, template_folder='templates')

@matches_blueprint.route('/', methods=['GET', 'POST'])
@ensure_correct_user
def index(user_id):
	if request.method == 'POST':
		form = MatchForm(request.form)
		if form.validate():
			try:
				new_match = Match(form.prompt_id.data, form.pick_id.data, form.start_time.data, form.end_time.data)
				db.session.add(new_match)
				db.session.commit()
				flash("Match Saved")
				return 'csrf_token'
			except IntegrityError as e:
				flash('Something Went Wrong')
				return 'oopse try again.'

	json_data = 'json_data'
	return render_template('matches/index.html', json_data=json_data)

@matches_blueprint.route('/new')
@ensure_correct_user
def new(user_id):
	form = MatchForm()
	json_data = 'json_data'
	return render_template('matches/new.html', form=form, json_data=json_data)

