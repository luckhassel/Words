class WordsSortUseCase:   
    def __init__(self, words: list[str], order: str): 
        self.words = words
        self.order = order
        
    def __is_order_reverse(self) -> bool:
        return self.order.lower() == "desc"
    
    def sort(self) -> list[str]:
        words_lower = [word.lower() for word in self.words]
        words_lower.sort(reverse=self.__is_order_reverse())
        
        return words_lower