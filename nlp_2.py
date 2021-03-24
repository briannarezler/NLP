from textblob import TextBlob
import nltk

# nlkt.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

"""
print(blob.words.count("juliet"))

print(blob.words.count("romeo"))

print(blob.words.count("thou"))

print(blob.words.count("joy"))

# print(blob.noun_phrases.count("lady capulet"))
"""

stops = stopwords.words("english")

more_stop_words = ["thee", "thy", "thou"]
stops += more_stop_words

items = blob.word_counts.items()
# print(items)

items = [item for item in items if item[0] not in stops]

# print(items[:10])


# Determining the top 20 words

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# print(sorted_items[:10])

top20 = sorted_items[1:21]
# print(top20)


# Convert top 20 to a dataframe

df = pd.DataFrame(top20, columns=["word", "count"])
# print(df)


# Plot on a bar graph

import matplotlib.pyplot as plt

df.plot.bar(
    x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)

plt.gcf().tight_layout()

# plt.show()


# WORDCLOUD

from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
# print(text)

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("done")
