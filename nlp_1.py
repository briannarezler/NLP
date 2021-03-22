# NLP stands for natural language processing
# can use it for web scraping, looking for keywords, sentiment analysis

from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

print(blob)

"""
print(blob.sentences)

print(blob.words)

print(blob.tags)

print(blob.noun_phrases)

print(blob.sentiment)

print(round(blob.sentiment.polarity, 3))
print(round(blob.sentiment.subjectivity, 3))

sentences = blob.sentences

for sentence in sentences:
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity, 3))
"""

# Try using a different analyzer instead

"""
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

print(blob.detect_language())

spanish = blob.translate(to="es")

print(spanish)
"""

# Pluralize and singularize
from textblob import Word

index = Word("index")

print(index.pluralize())

cacti = Word("cacti")

print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

# Spellcheck and correction
word = Word("theyr")

print(word.spellcheck())

print(word.correct())  # chooses word with the highest confidence value

sentence = TextBlob("Ths sentense has missplled wrds.")

print(sentence.correct())