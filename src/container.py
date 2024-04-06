'''Module for dependency injection'''

from dependency_injector import containers, providers
from use_cases.words_sort_use_case import WordsSortUseCase
from use_cases.words_vowel_count_use_case import WordsVowelCountUseCase

class Container(containers.DeclarativeContainer): # pylint: disable=too-few-public-methods
    '''Dependency injection container'''
    words_vowel_count_use_case = providers.Factory(WordsVowelCountUseCase)
    words_sort_use_case = providers.Factory(WordsSortUseCase)
