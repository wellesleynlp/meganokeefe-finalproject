#Full skeleton: given a single input text file, return top songs
#created 4/1

import argparse
import time
import pprint as pp
from os import listdir
from os.path import isfile, join
import rake
import musixmatch
import genius
import lyric_scraper
import operator
import random
from ngram import *
from corpus import *
import ast
from operator import itemgetter

def main(filepath):
    #Step 1- RAKE. returns a list of keyword phrases from the input text.
    def extractKeywords(filepath):
        rawtext = open(filepath).read()
        #rawtext = rawtext.decode("string_escape")
        #rawtext = rawtext.decode('utf-8')
        rake_object = rake.Rake("SmartStoplist.txt", 3, 2, 3)
        #each word has at least _ chars; each phrase has at most _ words, each keyword appears at least _ times.
        keywords = rake_object.run(rawtext)
        top = keywords[:10]
        #randomSample = [ keywords[i] for i in sorted(random.sample(xrange(len(keywords)), 15)) ]
        #just get the keywords themselves
        output = [item[0] for item in top]
        return output

    #Step 2 - API step. keywords -> set of song lyrics
    def songLyrics(filepath, keywords):
        rawSongs = musixmatch.get_all_songs(keywords) #musixmatch first
        print "\n\nRAW SONGS from MUSIXMATCH: ", len(rawSongs)

        songs = genius.get_all_songs(rawSongs)
        print "\n\nGENIUS GET", len(songs)

        lyricsDict = lyric_scraper.get_lyrics(songs)
        print "\n\nLYRICS DICT FROM GENIUS..."
        return lyricsDict

    #Step 3 - word model step using NGrams
    def getTopSongs(filepath, lyricsDict):
        print "\n\nCALCULATING C-E WITH ORIGINAL TEXT..."
        corpus = Corpus(filepath, casefold=True)
        wordmodel = NGram(1, 'word', 0.8, openvocab=False)
        ts = corpus.tokenized_sents
        wordmodel.estimate_from_text(ts)
        enum = lyricsDict.items()
        #song is (id, [title by, lyrics, url])
        entropies = []
        for song in enum:
            lyrics = song[1][1]
            titleBy = song[1][0]
            ce = wordmodel.cross_entropy(lyrics.split())
            entropies.append((titleBy, ce))
        ranked = sorted(entropies,key=itemgetter(1))
        return ranked

    kws = extractKeywords(filepath)
    lyrics = songLyrics(filepath, kws)
    return getTopSongs(filepath, lyrics)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("datadir", help="directory where dataset is located", type=str)
    args = parser.parse_args()
    start_time = time.time()
    results = main(args.datadir)
    print results, '\n\n'
    print("--- %s seconds ---" % (time.time() - start_time))
