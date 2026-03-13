## TDIDF --> Term Frequency and Inverse document frequency
## TDIF = TD * IDF
## Term Freq = number of repeatation of words in a sentence / no of words in sentence
## Inverse Doc Freq = loge(no of sentences/no os sentences containing teh word)

## step1- read data
## step2 - text preprocessing
## step3 - vectorizing

import pandas as pd
messages = pd.read_csv("spam.csv", names=['label', 'message'], encoding='latin-1')
print(messages.head(5))

## Data cleaning and Text preprocessing
## lemmatization, remove stopwords, lower all case, remove special chars
import re
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordlemmatize = WordNetLemmatizer()

# let us build a corpus which is our cleaned preprocessed messages
corpus=[]
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])# replace anything other than a-z , A-Z with blank
    review = review.lower()
    review =review.split() # convert it all to list of words
    review = [wordlemmatize.lemmatize(word) for word in review if not word in stopwords.words('english')] # take all words without stop words and apply stemming
    review = ' '.join(review) # join all these words to a sentence
    corpus.append(review) # append this review to corpus
##print("Corpus: \n\n",corpus) # you see huge list of sentences

## Create TDIDF and ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=100)
X=tfidf.fit_transform(corpus).toarray()

# add thsi for viewing
import numpy as np
np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" %x))
print("\n\n Vectorized X values now: ",X)
## in output you see list of vectors of zeros and som decimal values too
## decimal values indicate importance of some words
## sample o/p
#  [0 0 0 0 0 0 0 0 0.39 0 0 0 0 0 0.601 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ... 0.323 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.333 0 0 0 0 0 0 0 0.388 0 0 0 0 0 0]


## apply n grams
tfidf=TfidfVectorizer(max_features=100, ngram_range=(2,2))
X=tfidf.fit_transform(corpus).toarray()
np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" %x))

print("\n\n tfidf vocab lis: ",tfidf.vocabulary_)
print("\n\n Vectorized X values now with ngarm = 2,2: ",X)

