from flask import redirect, render_template, request, url_for, Blueprint, flash

responses_blueprint = Blueprint('responses', __name__, template_folder='templates')
