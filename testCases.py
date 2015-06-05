import os
import server
from server import app
import unittest
import tempfile
import  json
import random
from eve import Eve
import settings

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True

        self.app.config['MONGO_HOST'] = '10.240.115.93'
        self.app.config['MONGO_PORT'] = 27017
        self.app.config['MONGO_USERNAME'] = 'test'
        self.app.config['MONGO_PASSWORD'] = 'test'
        self.app.config['MONGO_DBNAME'] = 'test'

        self.app = server.app.test_client()


    """def tearDown(self):
        os.close(self.db_fd)
        os.unlink(server.app.config['DATABASE'])"""


    def test_login(self):
        email = 'dean.howard88@example.com'
        password = '111'
        response = self.app.post('/auth/login',
            data=json.dumps({
                'email': email,
                'password': password
            }), content_type='application/json')
        print response
        #json_data = json.loads(response.data)
        #print json_data
        #self.assertEqual(json_data['status_code'], 200)

        email = 'wrong_email@example.com'
        password = '222'
        response = self.app.post('/auth/login',
            data=json.dumps({
                'email': email,
                'password': password
            }), content_type='application/json')
        print response
        #json_data = json.loads(response.data)
        #print json_data
        #self.assertEqual(json_data['status_code'], 401)


    def test_register(self):

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
        print response
        #json_data = json.loads(response.data)
        #print json_data
        #self.assertEqual(json_data['status_code'], 200)

if __name__ == '__main__':
    unittest.main()