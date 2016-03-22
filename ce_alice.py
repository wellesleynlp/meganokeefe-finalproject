#Megan, 3/22
#practicing skeleton version of last part of algorithm (CE rank of songs on orig. text)
import pprint as pp
from ngram import *
from corpus import *
import rake_test
import genius
import lyric_scraper
import ast
from operator import itemgetter

#this will already have been done earlier
filename = "carroll-alice.txt"
corpus = Corpus(filename, casefold=True)

#make a model- for now, using unigrams- one song has few words!
wordmodel = NGram(1, 'word', 0.8, openvocab=False)
ts = corpus.tokenized_sents
wordmodel.estimate_from_text(ts)
"""
#get keywords
rawkw = rake_test.get_keywords(filename)[:10]
keywords = [item[0] for item in rawkw]

#get songs
songs = genius.get_all_songs(keywords)

#get lyrics using scraper
lyricsDict = lyric_scraper.get_lyrics(songs)

#write to file
with open("aliceLyrics.txt", "w") as outfile:
    outfile.write(str(lyricsDict))"""

#now get the lyrics and rank cross-entropies
with open("aliceLyrics.txt") as infile:
    lyricsDict = ast.literal_eval(infile.read())

all = lyricsDict.items()
#song is (id, [title by, lyrics, url])
entropies = []
for song in all:
    lyrics = song[1][1]
    titleBy = song[1][0]
    ce = wordmodel.cross_entropy(lyrics.split())
    entropies.append((titleBy, ce))

ranked = sorted(entropies,key=itemgetter(1))
topTen = ranked[:10]
pp.pprint(topTen)
