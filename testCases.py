import os
from server import *
import unittest
import json
import random

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_login(self):
        email = 'carole.gilbert16@example.com'
        password = '111'
        response = self.app.post('/auth/login',
            data=json.dumps({
                'email': email,
                'password': password
            }), content_type='application/json')

        self.assertEqual(response.status_code, 200)

        email = 'wrong_email@example.com'
        password = '222'
        response = self.app.post('/auth/login',
            data=json.dumps({
                'email': email,
                'password': password
            }), content_type='application/json')
        self.assertEqual(response.status_code, 401)


    """def test_register(self):

        email = 'testing_email'+str(random.randint(1, 101099245))+'@example.com'
        password = '111'
        firstname = 'firstname'
        lastname = 'lastname'
        username = 'satya'

        response = self.app.post('/auth/signup',
            data=json.dumps({
                'email': email,
                'password': password,
                'firstname':firstname,
                'lastname': lastname,
                'username':username
            }), content_type='application/json')
        print response.data
        #json_data = json.loads(response.data)
        #print json_data
        #self.assertEqual(json_data['status_code'], 200)"""

if __name__ == '__main__':
    unittest.main()