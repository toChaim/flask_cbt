from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.models import User
from project.users.forms import UserForm, UserLoginForm, UserDeleteForm
from project import db
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, current_user
from project.decorators import ensure_correct_user

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		form = UserForm(request.form)
		from IPython import embed; embed()
		if form.validate():
			try:
				new_user = User(form.data['first_name'],
					form.data['username'],
					form.data['password'])
				db.session.add(new_user)
				db.session.commit()
				login_user(new_user)
				flash("You have successfully signed up.")
				return redirect(url_for('users.show',id=new_user.id))
			except IntegrityError as e:
				flash("Username already taken.")
				return render_template('users/new.html', form=form)
		# form not vlalid
		else:
			flash("Invalid submission. Please try again.")
			return render_template('users/new.html', form=form), 422

	return render_template('users/index.html')

@users_blueprint.route('/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@users_blueprint.route('/logout')
def logout():
	flash('{} sucessfully loged out.'.format(current_user.username))
	logout_user()
	return redirect(url_for('users.index'))

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	form = UserLoginForm(request.form)

	if request.method == 'POST':
		user = User.authenticate(form.username.data, form.password.data)

		if form.validate() and user:
			login_user(user)
			flash('{} successfully logedin.'.format(user.first_name))
			return redirect(url_for('users.show', id=user.id))
		else:
			flash('NOT valid!!! BAD USER')
			return render_template('users/login.html', form=form)


	return render_template('users/login.html', form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_correct_user
def show(id):
	form = UserForm(request.form)
	d_form = UserDeleteForm(request.form)

	if request.method == b'PATCH':
		if form.validate():
			form.populate_obj(current_user)
			flash("Updatign {}'s profile.".format(current_user.username))
			db.session.add(current_user)
			db.session.commit()
			return redirect(url_for('users.show', id=current_user.id))
		else:
			return render_template('users/edit.html', id=current_user.id, form=form, d_form=d_form)

	if request.method == b'DELETE':
		if d_form.validate():
			db.session.delete(current_user)
			db.session.commit()
			flash('User DELETE')
			return redirect(url_for('users.index'))

	return render_template('users/show.html')

@users_blueprint.route('/<int:id>/edit')
@ensure_correct_user
def edit(id):
	form = UserForm(obj=current_user)
	d_form = UserDeleteForm()
	return render_template('users/edit.html', form=form, d_form=d_form)