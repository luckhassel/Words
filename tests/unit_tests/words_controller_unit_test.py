'''Words controller unit test'''

import json
import unittest
from app import app

class TestHomeView(unittest.TestCase):
    '''Words controller unit test'''
    _app = None

    @classmethod
    def setUpClass(cls):
        cls._app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls._app = None

    def test_get(self):
        '''Test health endpoint status code'''
        response = self._app.get('/')
        self.assertEqual(200, response.status_code)

    def test_html_string_response(self):
        '''Test health endpoint response data'''
        response = self._app.get('/')
        self.assertEqual("healthy", response.data.decode('utf-8'))

    def test_vowel_count_empty_content(self):
        '''Test vowel count endpoint getting empty content'''
        response = self._app.post('vowel_count')
        self.assertEqual(415, response.status_code)

    def test_vowel_count_wrong_content_type(self):
        '''Test vowel count endpoint getting wrong type content'''
        response = self._app.post('vowel_count', 'wrong content')
        self.assertEqual(415, response.status_code)

    def test_vowel_count_bad_request(self):
        '''Test vowel count endpoint getting bad request'''
        content = {"wordas": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_vowel_count_success(self):
        '''Test vowel count endpoint getting success response'''
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')

        expected_result = {"batman": 2, "robin": 2, "coringa": 3}

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))

    def test_vowel_count_success_content_type(self):
        '''Test vowel count endpoint getting success content type'''
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')

        expected_result = 'application/json'

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, response.content_type)

    def test_vowel_count_success_empty(self):
        '''Test vowel count endpoint getting empty response'''
        content = {"words": []}
        response = self._app.post('vowel_count', json=content, content_type='application/json')

        expected_result = {}

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))

    def test_vowel_count_fail(self):
        '''Test vowel count endpoint getting fail count'''
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')

        expected_result = {"batman": 2, "robin": 10, "coringa": 3}

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))


    def test_sort_empty_content(self):
        '''Test sort endpoint getting empty content'''
        response = self._app.post('sort')
        self.assertEqual(415, response.status_code)

    def test_sort_wrong_content_type(self):
        '''Test sort endpoint getting wrong content type'''
        response = self._app.post('sort', 'wrong content')
        self.assertEqual(415, response.status_code)

    def test_sort_bad_request(self):
        '''Test sort endpoint getting bad request'''
        content = {"wordas": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_sort_asc_success(self):
        '''Test sort endpoint getting success ordering ascending'''
        content = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')


        expected_result = ["batman", "coringa", "robin"]

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))

    def test_sort_asc_fail(self):
        '''Test sort endpoint failing ordering ascending'''
        content = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')


        expected_result = ["batman", "robin", "coringa"]

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))

    def test_sort_desc_success(self):
        '''Test sort endpoint getting success ordering descending'''
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')


        expected_result = ["robin", "coringa", "batman"]

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))

    def test_sort_desc_fail(self):
        '''Test sort endpoint failing ordering descending'''
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')


        expected_result = ["batman", "robin", "coringa"]

        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))

    def test_sort_success_content_type(self):
        '''Test sort endpoint getting success content type'''
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')

        expected_result = 'application/json'

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, response.content_type)

    def test_sort_success_empty(self):
        '''Test sort endpoint getting success empty content'''
        content = {"words": [], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')

        expected_result = []

        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))
