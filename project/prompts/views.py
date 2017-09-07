from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.decorators import ensure_correct_user
from flask_login import current_user
from project.prompts.forms import PromptForm, PromptDeleteForm
from project import db
from sqlalchemy.exc import IntegrityError
from project.models import Prompt

prompts_blueprint = Blueprint('prompts', __name__, template_folder='templates')

@prompts_blueprint.route('/', methods=['GET', 'POST'])
@ensure_correct_user
def index(user_id):
	if request.method == 'POST':
		form = PromptForm(request.form)
		if form.validate():
			try:
				new_prompt = Prompt(form.data['title'],
					form.data['affirmation'] or None, current_user.id)
				db.session.add(new_prompt)
				db.session.commit()
				flash("Prompt added.")
				return redirect(url_for('prompts.index',user_id=current_user.id))
			except IntegrityError as e:
				flash("Thought already taken.")
				return render_template('prompts/new.html', user_id=current_user, form=form)
		# form not vlalid
		else:
			flash("Invalid submission. Please try again.")
			return render_template('prompts/new.html', form=form)

	prompts_list = current_user.prompts
	return render_template('prompts/index.html', prompts_list=prompts_list)

@prompts_blueprint.route('/new')
@ensure_correct_user
def new(user_id):
	form = PromptForm(request.form)
	return render_template('prompts/new.html', form=form)

@prompts_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_correct_user
def show(user_id, id):
	prompt = Prompt.query.get(id)
	form = PromptForm(request.form)
	d_form = PromptDeleteForm(request.form)

	if request.method == b'PATCH':
		if form.validate():
			form.populate_obj(prompt)
			flash("Updatign {}'s profile.".format(prompt.title))
			db.session.add(prompt)
			db.session.commit()
			return redirect(url_for('prompts.show', user_id=current_user.id, id=id))
		else:
			return render_template('prompts/edit.html', user_id=current_user.id, id=id, form=form, d_form=d_form)

	if request.method == b'DELETE':
		if d_form.validate():
			db.session.delete(prompt)
			db.session.commit()
			flash('Prompt DELETE')
			return redirect(url_for('prompts.index', user_id=current_user.id))

	return render_template('prompts/show.html', prompt=prompt)

@prompts_blueprint.route('/<int:id>/edit')
@ensure_correct_user
def edit(user_id, id):
	prompt = Prompt.query.get(id)
	form = PromptForm(obj=prompt)
	d_form = PromptDeleteForm()
	return render_template('prompts/edit.html', prompt=prompt, form=form, d_form=d_form)
	