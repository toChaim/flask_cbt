from flask import redirect, render_template, request, url_for, Blueprint, session, flash
from project.models import User
from project.users.forms import UserForm

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/')
def index():
	return render_template('users/index.html')

@users_blueprint.route('/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)
