"""
Wordle object class
"""

from random import choice
import tools

import numpy as np


class Wordle:

    def __init__(self, letters=5):
        self.letters = letters
        self.state =  np.array([[0] * letters])
        self.all_words = tools.all_words(letters)
        self.word = choice(self.all_words) 
        self.possible_words = self.all_words

    def update_state(self, guess):
        """
        update self.state according to guess.
        """
        self.state = tools.new_state(self.state, self.word, guess)
     
    def update_possible_words(self, guess):
        """
        Update self.possible_words according to guess.
        """

    def guess(self, guess):
        """
        Make a guess on self.word.
        """

        self.update_state(guess)
        self.update_possible_words(guess)
        

