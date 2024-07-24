import nltk
from nltk.corpus import treebank
from nltk import bigrams
from collections import defaultdict, Counter

# Download required data
nltk.download('treebank')

# Load tagged sentences from the Penn Treebank corpus
tagged_sentences = treebank.tagged_sents()

# Extract tags and compute tag bigrams
tags = [tag for sent in tagged_sentences for _, tag in sent]
tag_bigrams = list(bigrams(tags))

# Count occurrences
tag_counts = Counter(tags)
bigram_counts = Counter(tag_bigrams)

# Calculate probabilities
tag_prob = defaultdict(lambda: defaultdict(lambda: 0))
for (prev_tag, tag), count in bigram_counts.items():
    tag_prob[prev_tag][tag] = count / tag_counts[prev_tag]

# Handle the case where a tag sequence was not seen during training
def get_tag_prob(prev_tag, tag):
    return tag_prob[prev_tag].get(tag, 0.0)

# Define the tagging function
def tag_sentence(sentence):
    tags = [None] * len(sentence)  # Initialize tags list
    if len(sentence) == 0:
        return []
    
    # Start with the most frequent tag
    tags[0] = max(tag_counts, key=tag_counts.get)
    
    for i in range(1, len(sentence)):
        prev_tag = tags[i - 1]
        max_prob = 0
        best_tag = None
        for tag in tag_counts:
            prob = get_tag_prob(prev_tag, tag)
            if prob > max_prob:
                max_prob = prob
                best_tag = tag
        tags[i] = best_tag
    
    return list(zip(sentence, tags))

# Test the tagging function
test_sentence = "This is a simple test".split()
tagged_sentence = tag_sentence(test_sentence)
print(tagged_sentence)
