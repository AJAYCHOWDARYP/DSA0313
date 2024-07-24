import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> DT NN | DT NNS
    VP -> V NP
    DT -> 'the' | 'a'
    NN -> 'cat' | 'dog'
    NNS -> 'cats' | 'dogs'
    V -> 'chased' | 'saw'
""")

# Create a parser
parser = ChartParser(grammar)

# Define a sentence
sentence = "the cat chased a dog".split()

# Parse the sentence and generate the parse tree
parse_trees = list(parser.parse(sentence))

# Visualize the parse tree
for tree in parse_trees:
    tree.pretty_print()
    tree.draw()
