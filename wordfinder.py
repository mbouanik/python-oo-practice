"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self):
        with open('words.txt', 'r') as file:
           self.rand_word = choice(file.readlines())