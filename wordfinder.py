"""Word Finder: finds random words from a dictionary.
    >>> word = WordFinder('words.txt')
    

    >>> word.random_word() in [word.strip() for word in open(word.file_name, 'r').readlines()]
    True

    >>> super_word =  SpecialWordFinder('food.txt')

    >>> super_word.special_word() in [word.strip() for word in open(super_word.file_name, 'r').readlines() if word and word[0] != '#']
    True

"""


from random import choice

class WordFinder:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def words_lst(self):
        with  open(self.file_name, 'r') as file:
            return [word.strip() for word in file.readlines()]
    
    def random_word(self):
        return choice(self.words_lst())


class SpecialWordFinder(WordFinder):
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def special_word(self):
        words_lst = super().words_lst()
        return choice([word for word in words_lst if word and word[0] != '#'])

