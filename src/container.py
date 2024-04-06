from dependency_injector import containers, providers
from use_cases.words_vowel_count_use_case import WordsVowelCountUseCase

class Container(containers.DeclarativeContainer):
    words_vowel_count_use_case = providers.Singleton(WordsVowelCountUseCase)