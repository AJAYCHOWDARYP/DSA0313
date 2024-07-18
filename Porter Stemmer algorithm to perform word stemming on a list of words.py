import nltk
from nltk import PorterStemmer
port=PorterStemmer()
word=input("enter input:")
stemmed=port.stem(word)
print(stemmed)
