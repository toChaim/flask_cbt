from project import app, db
from project.models import User, Prompt, Response, Match
from flask_testing import TestCase
import unittest
from bs4 import BeautifulSoup

class BaseTestCase(TestCase):
	def create_app(self):
		app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
		return app

	def setUp(self):
	 	db.create_all()
	# 	person1 = User("Elie", "Schoppik", "p")
	# 	person2 = User("Tim", "Garcia", "q")
	# 	person3 = User("Matt", "Lane", "123")
	# 	db.session.add_all([person1, person2, person3])
	# 	db.session.commit()

	def tearDown(self):
	 	db.drop_all()

	def test_index(self):
		response = self.client.get('/', follow_redirects=True, content_type='html/text')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Welcome to my little game.', response.data)

	def test_new(self):
		# check if route exists and has some important features
		response = self.client.get('/users/new', content_type='html/text')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Signing up for my little game.', response.data)
		self.assertIn(b'csrf_token', response.data)
		soup = BeautifulSoup(response.data, "html.parser")
		csrf_token = soup.find(id='csrf_token')['value']
		response = self.client.post(
			'/users/',
			data=dict(first_name="New", username="Student", password="p", confirm="p", csrf_token=csrf_token),
			follow_redirects=True
			)
		self.assertEqual(response.status_code, 200)
		self.assertNotIn(b'Invalid submission. Please try again.', response.data)
		self.assertIn(b'Logout', response.data)

	def test_bad_new_user(self):
		#  check that a user can't be created without a csrf_token
		response = self.client.post(
			'/users/',
			data=dict(first_name="New", username="Student", password="p", confirm="p"),
			follow_redirects=False
			)
		self.assertNotEqual(response.status_code, 200)
		self.assertIn(b'Invalid submission. Please try again.', response.data)
		self.assertNotIn(b'Logout', response.data)

	def test_404(self):
		response = self.client.get('/this_is_a_bad_route', content_type='html/text')
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.main()