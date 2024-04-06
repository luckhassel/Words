import json
from app import app
import unittest


class TestHomeView(unittest.TestCase):
    _app = None
    
    @classmethod
    def setUpClass(cls):
        cls._app = app.test_client()
        
    @classmethod
    def tearDownClass(cls):
        cls._app = None

    def test_get(self):
        response = self._app.get('/')
        self.assertEqual(200, response.status_code)

    def test_html_string_response(self):
        response = self._app.get('/')
        self.assertEqual("healthy", response.data.decode('utf-8'))
        
    def test_vowel_count_empty_content(self):
        response = self._app.post('vowel_count')
        self.assertEqual(415, response.status_code)
        
    def test_vowel_count_wrong_content_type(self):
        response = self._app.post('vowel_count', 'wrong content')
        self.assertEqual(415, response.status_code)
        
    def test_vowel_count_bad_request(self):
        content = {"wordas": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        self.assertEqual(400, response.status_code)
        
    def test_vowel_count_success(self):
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        
        expected_result = {"batman": 2, "robin": 2, "coringa": 3}
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))
        
    def test_vowel_count_success_content_type(self):
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        
        expected_result = 'application/json'
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, response.content_type)
        
    def test_vowel_count_success_empty(self):
        content = {"words": []}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        
        expected_result = {}
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))
        
    def test_vowel_count_fail(self):
        content = {"words": ["batman", "robin", "coringa"]}
        response = self._app.post('vowel_count', json=content, content_type='application/json')
        
        expected_result = {"batman": 2, "robin": 10, "coringa": 3}
        
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))
    
    
    def test_sort_empty_content(self):
        response = self._app.post('sort')
        self.assertEqual(415, response.status_code)
        
    def test_sort_wrong_content_type(self):
        response = self._app.post('sort', 'wrong content')
        self.assertEqual(415, response.status_code)
        
    def test_sort_bad_request(self):
        content = {"wordas": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        self.assertEqual(400, response.status_code)
        
    def test_sort_asc_success(self):
        content = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        
        expected_result = ["batman", "coringa", "robin"]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))
        
    def test_sort_asc_fail(self):
        content = {"words": ["batman", "robin", "coringa"], "order": "asc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        
        expected_result = ["batman", "robin", "coringa"]
        
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))
        
    def test_sort_desc_success(self):
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        
        expected_result = ["robin", "coringa", "batman"]
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))
        
    def test_sort_desc_fail(self):
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        
        expected_result = ["batman", "robin", "coringa"]
        
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(expected_result, json.loads(response.data))
        
    def test_sort_success_content_type(self):
        content = {"words": ["batman", "robin", "coringa"], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        expected_result = 'application/json'
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, response.content_type)
        
    def test_sort_success_empty(self):
        content = {"words": [], "order": "desc"}
        response = self._app.post('sort', json=content, content_type='application/json')
        
        expected_result = []
        
        self.assertEqual(200, response.status_code)
        self.assertEqual(expected_result, json.loads(response.data))