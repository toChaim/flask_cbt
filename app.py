from project import app
import os

if os.environ.get('ENV') == 'production':
  app.config_from_object('config.ProductionConfig')
else:
  app.config_from_object('config.DevelopmentConfig')