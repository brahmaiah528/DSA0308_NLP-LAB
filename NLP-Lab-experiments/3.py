import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lem = WordNetLemmatizer()

words = input("Enter a word: ")

for word in words:
    print(word, "->", lem.lemmatize(word, pos="v"))
