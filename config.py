import os

class Config():
	DEBUG = True
	SQLALCHEMY_ECHO = True
	PORT = 3000
	SQLALCHEMY_DATABASE_URI = "postgres://localhost/flask_cbt"
	SECRET_KEY = 'SECRET_KEY'
	TESTING = True

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_ECHO = False
	PORT = os.environ.get('PORT')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
	SECRET_KEY =os.environ.get('SECRET_KEY')
	TESTING = True
