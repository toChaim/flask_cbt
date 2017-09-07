from flask import redirect, render_template, request, url_for, Blueprint, flash, jsonify
from project.decorators import ensure_correct_user
from project.models import Match, User
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

	prompts = User.query.get(user_id).prompts
	json_data = []
	for p in prompts:
		responses = p.responses
		p_responses = []
		for r in responses:
			p_responses.append({ 'id': r.id, 'title': r.title, 'affirmation': r.affirmation, 'prompt_id': r.prompt_id })

		json_data.append({ 'id': p.id, 'title': p.title, 'affirmation': p.affirmation, 'user_id': p.user_id, 'responses': p_responses })
	
	return jsonify(json_data)

@matches_blueprint.route('/new')
@ensure_correct_user
def new(user_id):
	form = MatchForm()
	json_data = 'json_data'
	return render_template('matches/new.html', form=form, user_id=user_id)

