from functools import wraps
from flask_login import logout_user, current_user
from flask import redirect, url_for, flash

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # in the params we have something called id, is it the same as the user logged in?
        if kwargs.get('id') != current_user.id:
            # if not, redirect them back home
            flash("Not Authorized")
            logout_user()
            return redirect(url_for('users.login'))
        # otherwise, move on with all the arguments passed in!
        return fn(*args, **kwargs)
    return wrapper