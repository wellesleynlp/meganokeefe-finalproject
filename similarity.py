#TFIDF and Cosine Similarity for the song lyrics

from sklearn.feature_extraction.text import TfidfVectorizer
from os import listdir
from os.path import isfile, join
import numpy as np
import json

def getRankings(rawtext, lyricsDict):
    npath = "leaves.txt"
    novel = open(npath).read().decode('unicode_escape').encode('ascii','ignore')
    #text_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #documents = [novel] + [open(join(mypath,f)).read().decode('unicode_escape').encode('ascii','ignore') for f in text_files]

    #use lyrics handed off - get list of just the lyrics
    with open('leaves_lyrics.json', 'r') as fp:
        data = json.load(fp)

    songs = data.items()
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

print getRankings("", "")
