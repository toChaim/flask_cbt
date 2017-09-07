from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.decorators import ensure_correct_user
from project.responses.forms import ResponseForm, ResponseDeleteForm
from project.models import Prompt, Response
from project import db
from sqlalchemy.exc import IntegrityError
from flask_login import current_user

responses_blueprint = Blueprint('responses', __name__, template_folder='templates')

@responses_blueprint.route('/', methods=['POST'])
@ensure_correct_user
def index(user_id, prompt_id):
	prompt = Prompt.query.get(prompt_id)

	form = ResponseForm(request.form)
	if form.validate():
		try:
			new_response = Response(form.data['title'],
				form.data['affirmation'] or None, prompt_id)
			db.session.add(new_response)
			db.session.commit()
			flash("Response added.")
			return redirect(url_for('prompts.show',user_id=current_user.id, id=prompt_id))
		except IntegrityError as e:
			flash("That Response thought already taken.")
			return render_template('responses/new.html', form=form, prompt=prompt)
	# form not vlalid
	else:
		flash("Invalid submission. Please try again.")
		return render_template('responses/new.html', form=form, prompt=prompt)

@responses_blueprint.route('/new')
@ensure_correct_user
def new(user_id, prompt_id):
	prompt = Prompt.query.get(prompt_id)

	form = ResponseForm(request.form)
	return render_template('responses/new.html', form=form, prompt=prompt)

@responses_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_correct_user
def show(user_id, prompt_id, id):
	response = Response.query.get(id)
	form = ResponseForm(request.form)
	d_form = ResponseDeleteForm(request.form)

	if request.method == b'PATCH':
		if form.validate():
			form.populate_obj(response)
			flash("Updatign {}'s profile.".format(response.title))
			db.session.add(response)
			db.session.commit()
			return redirect(url_for('responses.show', user_id=user_id, prompt_id=prompt_id, id=id))
		else:
			return render_template('responses/edit.html', user_id=user_id, prompt_id=prompt_id, id=id, form=form, d_form=d_form)

	if request.method == b'DELETE':
		if d_form.validate():
			db.session.delete(response)
			db.session.commit()
			flash('Prompt DELETE')
			return redirect(url_for('prompts.show', user_id=current_user.id, id=prompt_id))

	return render_template('responses/show.html', response=response)

@responses_blueprint.route('/<int:id>/edit')
@ensure_correct_user
def edit(user_id, prompt_id, id):
	response = Response.query.get(id)
	form = ResponseForm(obj=response)
	d_form = ResponseDeleteForm()
	return render_template('responses/edit.html', response=response, form=form, d_form=d_form)
