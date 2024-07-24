import nltk
from nltk import CFG
from nltk.parse import pchart

# Define the grammar with probabilities
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.5] | V [0.2] | VP PP [0.3]
    V -> 'saw' [0.5] | 'ate' [0.3] | 'walked' [0.2]
    NP -> 'John' [0.3] | 'Mary' [0.3] | 'Bob' [0.2] | Det N [0.2]
    Det -> 'a' [0.5] | 'an' [0.3] | 'the' [0.2]
    N -> 'dog' [0.5] | 'cat' [0.5]
    PP -> P NP [1.0]
    P -> 'with' [0.6] | 'under' [0.4]
""")

# Define the sentence to parse
sentence = 'John saw the dog with the cat'.split()

# Use a probabilistic chart parser
parser = pchart.InsideChartParser(grammar)

# Parse the sentence
parses = list(parser.parse(sentence))

# Print the parse trees and their probabilities
for tree in parses:
    print(tree)
    print("Probability:", tree.prob())

# Note: Since NLTK's pchart parser does not directly support PCFG, we use a PCFG grammar 
# with the InsideChartParser. This will still give us probabilistic parse trees.
