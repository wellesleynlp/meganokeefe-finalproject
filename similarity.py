#TFIDF and Cosine Similarity for the song lyrics

from sklearn.feature_extraction.text import TfidfVectorizer
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd

def getRankings(npath, mypath):
    novel = open(npath).read().decode('unicode_escape').encode('ascii','ignore')
    text_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    documents = [novel] + [open(join(mypath,f)).read().decode('unicode_escape').encode('ascii','ignore') for f in text_files]
    tfidf = TfidfVectorizer().fit_transform(documents)
    pairwise_similarity = tfidf * tfidf.T
    pairwise_similarity = np.array(pairwise_similarity)
    #want the first row- similarity between the 0th item (the novel) and all the others
    pa = pairwise_similarity.tolist()
    pa = np.array(pa)
    ser = pd.Series(pa[0])
    print ser

print getRankings("leaves.txt", "leaves")
