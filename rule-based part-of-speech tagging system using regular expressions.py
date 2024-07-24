import re

# Define regular expression patterns for each POS tag
patterns = {
    'NN': r'\b\w*(tion|ment|ness)\b',   # Nouns
    'VB': r'\b\w*(ing|ed)\b',           # Verbs
    'JJ': r'\b\w*(y|ful)\b',            # Adjectives
    'RB': r'\b\w*ly\b',                 # Adverbs
}

def pos_tag(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # List to store tagged words
    tagged_words = []

    # Tag each word
    for word in words:
        tagged = False
        for tag, pattern in patterns.items():
            if re.search(pattern, word):
                tagged_words.append((word, tag))
                tagged = True
                break
        if not tagged:
            tagged_words.append((word, 'NN'))  # Default to noun if no pattern matches

    return tagged_words

# Example usage
sentence = "The quick brown fox jumps over the lazy dogs"
print(pos_tag(sentence))
