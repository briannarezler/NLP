# Create a wordcloud of the top 15 words that are the most recurring.
# Make sure to remove all stop words. Use only noun words for this analysis.
from textblob import TextBlob
from nltk import pos_tag, word_tokenize

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("book of John text.txt").read_text())

stops = stopwords.words("english")

more_stop_words = ["thy", "ye", "verily", "thee", "hath", "thou", "say", "art", "shall"]
stops += more_stop_words

noun_phrases = blob.noun_phrases

items = blob.word_counts.items()

items = [item for item in items if item[0] not in stops if item[0] in noun_phrases]


from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

top15 = list(sorted_items[0:15])
# print(top15)

my_words = ""
for p in top15:
    my_words += p[0] + " "
print(my_words)

from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt

wordcloud = WordCloud(
    stopwords=stops, colormap="Blues", background_color="gray", max_words=15
)

wordcloud = wordcloud.generate(my_words)

wordcloud = wordcloud.to_file("BookOfJohnCloud.png")

plt.imshow(wordcloud)
print("done")
