#TFIDF and Cosine Similarity for the song lyrics

from sklearn.feature_extraction.text import TfidfVectorizer
from os import listdir
from os.path import isfile, join
import numpy as np

def getRankings(novel, lyricsDict):
    songs = lyricsDict.items()
    lyrics = [d[1][1] for d in songs]
    #songs[i][0] accesses the artist+title of lyrics[i]
    documents = [novel] + lyrics
    tfidf = TfidfVectorizer().fit_transform(documents)
    pairwise_similarity = tfidf * tfidf.T
    #want the first row- similarity between the 0th item (the novel) and all the others
    z = pairwise_similarity[0]
    sims = np.array(z.toarray())
    #sims[i] is the cosine similarity between the Novel and the ith song lyric
    #smaller cosine sim -> greater similarity
    maxes = sims.argsort()[-10:][::-1] #gets minima
    tops = maxes[0][:15] #returns song indices """
    artitles = [songs[i][1][0] for i in tops]
    return artitles
