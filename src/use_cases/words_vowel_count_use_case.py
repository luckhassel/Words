class WordsVowelCountUseCase:   
    def __init__(self, words: list[str]): 
        self.words = words
    
    def vowel_count(self) -> dict:
        result = {}
        
        if self.words.count == 0:
            return result
        
        for i in range(0, len(self.words)):
            word_lower = self.words[i].lower()
            result[self.words[i]] = len([c for c in word_lower if c in 'aeiou'])
        
        return result