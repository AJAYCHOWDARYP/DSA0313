import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download the necessary NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = pos_tag(words)

# Print the POS tags
print("POS Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
