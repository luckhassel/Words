'''Test Words Vowel Count Use Case'''

import unittest
from use_cases.words_vowel_count_use_case import WordsVowelCountUseCase
from container import Container

class TestWordsVowelCountUseCase(unittest.TestCase):
    '''Test Words Vowel Count Use Case'''
    _container = None

    @classmethod
    def setUpClass(cls):
        cls._container = Container()

    @classmethod
    def tearDownClass(cls):
        cls._container = None

    def test_vowel_count_success(self):
        '''Test Words vowel count success'''
        data = ["batman", "robin", "coringa"]
        instance = self._container.words_vowel_count_use_case(data)

        result = instance.vowel_count()

        expected_result = {"batman": 2, "robin": 2, "coringa": 3}
        self.assertEqual(result, expected_result)

    def test_vowel_count_wrong_count(self):
        '''Test Words vowel count fail'''
        data = ["batman", "robin", "coringa"]
        instance = self._container.words_vowel_count_use_case(data)

        result = instance.vowel_count()

        expected_result = {"batman": 2, "robin": 1, "coringa": 3}
        self.assertNotEqual(result, expected_result)

    def test_vowel_count_empty_list(self):
        '''Test Words vowel count empty list'''
        data = []
        instance = self._container.words_vowel_count_use_case(data)

        result = instance.vowel_count()

        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_vowel_count_no_vowels(self):
        '''Test Words vowel count no vowels'''
        data = ["btmn", "rbn", "crng"]
        instance = self._container.words_vowel_count_use_case(data)

        result = instance.vowel_count()

        expected_result = {"btmn": 0, "rbn": 0, "crng": 0}
        self.assertEqual(result, expected_result)

    def test_vowel_count_no_vowels_partial(self):
        '''Test Words vowel count no vowels partial'''
        data = ["btmn", "rbn", "crnga"]
        instance = self._container.words_vowel_count_use_case(data)

        result = instance.vowel_count()

        expected_result = {"btmn": 0, "rbn": 0, "crnga": 1}
        self.assertEqual(result, expected_result)

    def test_vowel_count_instance(self):
        '''Test Words vowel count instance'''
        data = ["btmn", "rbn", "crnga"]
        instance = self._container.words_vowel_count_use_case(data)

        self.assertIsInstance(instance, WordsVowelCountUseCase)



if __name__ == '__main__':
    unittest.main()
