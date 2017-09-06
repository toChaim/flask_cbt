from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.decorators import ensure_correct_user
from flask_login import current_user
from project.prompts.forms import PromptForm

prompts_blueprint = Blueprint('prompts', __name__, template_folder='templates')

@prompts_blueprint.route('/', methods=['GET', 'POST'])
@ensure_correct_user
def index(user_id):
	# if request.method == 'POST':
	# 	form = UserForm(request.form)
	# 	if form.validate():
	# 		try:
	# 			new_user = User(form.data['first_name'],
	# 				form.data['username'],
	# 				form.data['password'])
	# 			db.session.add(new_user)
	# 			db.session.commit()
	# 			login_user(new_user)
	# 			flash("You have successfully signed up.")
	# 			return redirect(url_for('users.show',id=new_user.id))
	# 		except IntegrityError as e:
	# 			flash("Username already taken.")
	# 			return render_template('users/new.html', form=form)
	# 	# form not vlalid
	# 	else:
	# 		flash("Invalid submission. Please try again.")
	# 		return render_template('users/new.html', form=form)

	prompts_list = current_user.prompts
	return render_template('prompts/index.html', prompts_list=prompts_list)

@prompts_blueprint.route('/new')
def new(user_id):
	form = PromptForm(request.form)
	return render_template('prompts/new.html', form=form)

