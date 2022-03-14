import json
from string import ascii_lowercase as letters

import pandas as pd
from bokeh.plotting import figure, show

# Load dictionary
with open("dictionary.json", "r") as f:
        dictionary = json.load(f)
words = list(dictionary.keys()) #list of words (dict keys)
quordle_words = [w for w in words if len(w) == 5] # subset words of 5 letters

# Count occurrences of each letter
all_letters = "".join(quordle_words)
letter_counts = [all_letters.count(l) for l in letters]
letter_counts = (
        pd.DataFrame({"letter": list(letters), "n": letter_counts})
        .sort_values("n", ascending=False, ignore_index=True)
        )
letter_counts["frac"] = letter_counts.n / len(all_letters)*100

# Show figure of letter counts
f = figure(x_range=letter_counts.letter)
f.vbar(x=letter_counts.letter, top=letter_counts.frac, width=0.9)
show(f)
