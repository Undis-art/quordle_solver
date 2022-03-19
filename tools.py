import json
from string import ascii_lowercase as letters

def all_words(n=5):

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
