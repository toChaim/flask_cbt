import os

class Config():
	DEBUG = True
	SQLALCHEMY_ECHO = True
	PORT = 3000
	SQLALCHEMY_DATABASE_URI = "postgres://localhost/flask_cbt"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SECRET_KEY = 'SECRET_KEY'
	TESTING = True

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_ECHO = False
	PORT = os.environ.get('PORT')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY =os.environ.get('SECRET_KEY')
	TESTING = True
