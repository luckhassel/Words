'''Use case for counting vowels on each word'''

class WordsVowelCountUseCase:
    '''Use case for counting vowels on each word'''
    def __init__(self, words: list[str]):
        self.words = words

    def vowel_count(self) -> dict:
        '''Counts vowel on each word specified on constructor'''
        result = {}

        if self.words.count == 0:
            return result

        for i in enumerate(self.words):
            word_lower = self.words[i].lower()
            result[self.words[i]] = len([c for c in word_lower if c in 'aeiou'])

        return result
