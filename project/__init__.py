#imports, settings, functions, blueprints
#imports
from flask import Flask, url_for
from flask_modus import Modus
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os

#settings
app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)

if os.environ.get('ENV') == 'production':
  app.config.from_object('config.ProductionConfig')
else:
  app.config.from_object('config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Please log in!'

#functions
@app.context_processor #http://flask.pocoo.org/snippets/40/
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

#blueprints
from project.users.views import users_blueprint
from project.prompts.views import prompts_blueprint
from project.responses.views import responses_blueprint
from project.matches.views import matches_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(prompts_blueprint, url_prefix="/users/<int:user_id>/prompts")
app.register_blueprint(responses_blueprint, url_prefix="/users/<int:user_id>/prompts/<int:prompt_id>/responses")
app.register_blueprint(matches_blueprint, url_prefix="/users/<int:user_id>/matches")