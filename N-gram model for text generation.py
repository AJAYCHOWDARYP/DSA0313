import random
from collections import defaultdict, Counter

def preprocess_text(text):
    # Convert text to lowercase and split into words
    return text.lower().split()

def build_bigram_model(words):
    bigrams = list(zip(words[:-1], words[1:]))
    bigram_model = defaultdict(Counter)
    
    for w1, w2 in bigrams:
        bigram_model[w1][w2] += 1
    
    # Convert counts to probabilities
    for w1, w2_counter in bigram_model.items():
        total_count = sum(w2_counter.values())
        for w2 in w2_counter:
            w2_counter[w2] /= total_count
    
    return bigram_model

def generate_text(bigram_model, seed_word, length=50):
    current_word = seed_word
    generated_words = [current_word]
    
    for _ in range(length - 1):
        next_words = bigram_model.get(current_word, {})
        if not next_words:
            break
        next_word = random.choices(list(next_words.keys()), list(next_words.values()))[0]
        generated_words.append(next_word)
        current_word = next_word
    
    return ' '.join(generated_words)

# Example usage
text = """
Your sample text goes here. Replace this with your own corpus to train the bigram model.
The more diverse and large the corpus, the better the generated text will be.
"""

words = preprocess_text(text)
bigram_model = build_bigram_model(words)
seed_word = 'your'  # Choose a seed word from your text
generated_text = generate_text(bigram_model, seed_word, length=20)

print(generated_text)
