# Create a wordcloud of the top 15 words that are the most recurring.
# Make sure to remove all stop words. Use only noun words for this analysis.
from textblob import TextBlob
import nltk

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("book of John text.txt").read_text())

stops = stopwords.words("english")

items = blob.word_counts.items()
# print(items)

items = [item for item in items if item[0] not in stops]

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

top15 = sorted_items[1:16]


from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt

text = Path("book of John text.txt").read_text()
# print(text)

wordcloud = WordCloud(colormap="prism", background_color="white", max_words=15)

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("BookOfJohnCloud.png")

plt.imshow(wordcloud)
print("done")
