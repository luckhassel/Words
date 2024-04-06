'''Test Sort Use Case'''

import unittest
from use_cases.words_sort_use_case import WordsSortUseCase
from container import Container

class TestWordsSortUseCase(unittest.TestCase):
    '''Test Sort Use Case'''
    _container = None

    @classmethod
    def setUpClass(cls):
        cls._container = Container()

    @classmethod
    def tearDownClass(cls):
        cls._container = None

    def test_sort_asc_success(self):
        '''Test Sort ascending success'''
        data = ["batman", "robin", "coringa"]
        order = "asc"
        instance = self._container.words_sort_use_case(data, order)

        result = instance.sort()

        expected_result = ["batman", "coringa", "robin"]
        self.assertEqual(result, expected_result)

    def test_sort_desc_success(self):
        '''Test Sort descending success'''
        data = ["batman", "robin", "coringa"]
        order = "desc"
        instance = self._container.words_sort_use_case(data, order)

        result = instance.sort()

        expected_result = ["robin", "coringa", "batman"]
        self.assertEqual(result, expected_result)

    def test_sort_asc_fail(self):
        '''Test Sort ascending fail'''
        data = ["batman", "robin", "coringa"]
        order = "asc"
        instance = self._container.words_sort_use_case(data, order)

        result = instance.sort()

        expected_result = ["batman", "robin", "coringa"]
        self.assertNotEqual(result, expected_result)

    def test_sort_desc_fail(self):
        '''Test Sort descending success'''
        data = ["batman", "robin", "coringa"]
        order = "desc"
        instance = self._container.words_sort_use_case(data, order)

        result = instance.sort()

        expected_result = ["coringa", "robin", "batman"]
        self.assertNotEqual(result, expected_result)

    def test_sort_empty(self):
        '''Test Sort empty success'''
        data = []
        order = "desc"
        instance = self._container.words_sort_use_case(data, order)

        result = instance.sort()

        expected_result = []
        self.assertEqual(result, expected_result)

    def test_sort_instance(self):
        '''Test Sort instance'''
        data = []
        order = "desc"
        instance = self._container.words_sort_use_case(data, order)

        self.assertIsInstance(instance, WordsSortUseCase)

if __name__ == '__main__':
    unittest.main()
