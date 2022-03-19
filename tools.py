import json
from string import ascii_lowercase as letters

import numpy as np

def all_words(n=5):
    """ List all n letters long words in dictionary."""

    # Load dictionary
    with open("dictionary.json", "r") as f:
            dictionary = json.load(f)

    # List words (dict keys)
    words = list(dictionary.keys()) 
    
    # Choose words of right length
    words_len5 = [w for w in words if len(w) == n]

    # Drop words with any special characters
    nrdle_words = [w for w in words_len5 if all([c in letters for c in w])]

    return nrdle_words

def new_state(state, word, guess):
    """
    Generate updated state for wordle guesses according to previous state,
    the word (to be guessed) and given guess.
    """

    # Make the new row of info
    new_row = np.array([match(guess, word)])

    return np.concatenate((state, new_row), axis=0)
    
def match(guess, word):
    """
    Describe correctness of word in argument "guess" compared to word in
    argument "word".
    0: Letter doesn't appear in word.
    1: Letter appears in the word, but in different location.
    2: Letter appears in the word, and in the same location.
    """

    n = len(word)

    # Use numpy arrays for convenience
    word_arr = np.array(list(word))
    guess_arr = np.array(list(guess))
    
    # Initialize with all zeros
    match = np.array([0] * n)

    # Mark right letters in right places
    right_place = word_arr == guess_arr
    match[right_place] = 2

    def _all_marked(l):
        """
        Tell whether a letter has already been marked in match-array as many
        times as it occurs in word.
        """
        # List letters that have been marked with 2 or 1 so far
        all_marked_letters = guess_arr[match != 0]

        # Count previously marked occurrences of l
        n_marked = np.array(all_marked_letters == l).sum()
        
        # Count occurrences of l in word
        n_in_word = (word_arr == l).sum()

        if n_marked == n_in_word:
            return True
        else:
            return False

    not_exact_matches = np.where(match != 2)[0]

    # Mark right letters in wrong places
    for i in not_exact_matches:
        if guess_arr[i] in word_arr and not _all_marked(guess[i]):
            match[i] = 1

    return match

