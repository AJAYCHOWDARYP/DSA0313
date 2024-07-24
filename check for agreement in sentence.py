import nltk
from nltk import CFG

# Define the CFG for a simple grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> DT NN | DT JJ NN
    VP -> VBZ NP
    DT -> 'the' | 'a'
    JJ -> 'big' | 'small'
    NN -> 'dog' | 'cat'
    VBZ -> 'chases' | 'sees'
""")

# Create a parser
parser = nltk.ChartParser(grammar)

# Function to check agreement in sentences
def check_agreement(sentence):
    words = sentence.split()
    try:
        parse_tree = next(parser.parse(words))
        print(f"Sentence: '{sentence}' is grammatically correct.")
        parse_tree.pretty_print()
    except StopIteration:
        print(f"Sentence: '{sentence}' is not grammatically correct.")

# Test sentences
sentences = [
    "the dog chases a cat",
    "a big dog sees the small cat",
    "the cat sees a big dog",
    "dog the chases cat a"  # Incorrect sentence
]

for sentence in sentences:
    check_agreement(sentence)
