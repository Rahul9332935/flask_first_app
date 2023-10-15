import unittest
from flask import Flask, jsonify
import app  # Your Flask application


class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.app_context = app.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_save_user(self):
        data = {
            "name": "John Doe",
            "mobile": "1234567890",
            "email": "john@example.com",
            "password": "password123"
        }
        response = self.app.post('/user/create', json=data)
        self.assertEqual(response.status_code, 200)

    def test_check_mobile_exists(self):
        response = self.app.get('/user/checkMobile/1454738996')
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertTrue(data['result'])

    def test_check_email_exists(self):
        response = self.app.get('/user/checkEmail/an45ek5it4@ex1ample.com')
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertTrue(data['result'])

    def test_login_using_email(self):
        data = {
            "email": 'rahul@gmail.com',
            "password": "password123"
        }
        response = self.app.post('/user/login/UsingEmail', json=data)
        self.assertEqual(response.status_code, 200)

    def test_login_using_mobile(self):
        data = {
            "mobile": "9648472430",
            "password": "passwo5rd123"
        }
        response = self.app.post('/user/login/UsingMobile', json=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__test_app__':
    unittest.main()
