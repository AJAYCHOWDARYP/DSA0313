# Define transformation rules
transform_rules = {
    "NOUN": {"endswith": ["ing"], "transform_to": "VERB"},
    "ADJ": {"startswith": ["un"], "transform_to": "NEG"},
    "ADV": {"endswith": ["ly"], "transform_to": "ADV"},
    "DET": {"exact_match": ["the", "a", "an"], "transform_to": "DET"}
}

# Function to apply transformation rules and tag words
def transform_based_tagging(words, rules):
    tagged_words = []
    for word in words:
        tagged = False
        for tag, rule in rules.items():
            if "endswith" in rule:
                if any(word.endswith(suffix) for suffix in rule["endswith"]):
                    tagged_words.append((word, rule["transform_to"]))
                    tagged = True
                    break
            elif "startswith" in rule:
                if any(word.startswith(prefix) for prefix in rule["startswith"]):
                    tagged_words.append((word, rule["transform_to"]))
                    tagged = True
                    break
            elif "exact_match" in rule:
                if word in rule["exact_match"]:
                    tagged_words.append((word, rule["transform_to"]))
                    tagged = True
                    break
        if not tagged:
            tagged_words.append((word, "UNK"))  # Default tag for unknown words
    return tagged_words

# Example usage
sentence = "The running fox jumps over the lazy dog"
words = sentence.lower().split()

tagged_words = transform_based_tagging(words, transform_rules)
print(tagged_words)
