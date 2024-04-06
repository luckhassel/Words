'''Use case for sorting words'''

class WordsSortUseCase: # pylint: disable=too-few-public-methods
    '''Use case for sorting words'''
    def __init__(self, words: list[str], order: str):
        self.words = words
        self.order = order

    def __is_order_reverse(self) -> bool:
        return self.order.lower() == "desc"

    def sort(self) -> list[str]:
        '''Sort all words intialized on constructor, following the order also defined there'''
        words_lower = [word.lower() for word in self.words]
        words_lower.sort(reverse=self.__is_order_reverse())

        return words_lower
