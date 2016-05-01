#Full skeleton: given a single input text file, return top songs
#last update: 5/1/16

import argparse
import time
import re
import pprint as pp
from collections import Counter
from os import listdir
from os.path import isfile, join
import rake
import musixmatch
import genius
import lyric_scraper
import operator
from ngram import *
from corpus import *
import ast
from operator import itemgetter

def main(filepath):
    #Step 1- RAKE. returns a list of top 10 key phrases from the input text.
    def extractKeywords(text):
        rake_object = rake.Rake("SmartStoplist.txt", 4, 3, 5)
        #each word has at least _ chars; each phrase has at most _ words, each keyword appears at least _ times.
        keywords = rake_object.run(text)
        #pp.pprint(keywords)
        top = keywords[:5] #only get top 5 for now
        output = [item[0] for item in top]
        return output

    #Step 1A- proper noun extraction
    def properNouns(text):
        text = text.replace("\n", " ")
        twos = re.findall('([A-Z][a-z]+(?=\s[A-Z])(?:\s[A-Z][a-z]+)+)', text)
        topTwos = Counter(twos).most_common(20)
        ones = re.findall(r'(?<!\.\s)\b[A-Z][a-z]*\b', text)
        topOnes = Counter(ones).most_common(20)
        tops = topOnes + topTwos
        #filter stopwords
        with open("SmartStoplist.txt", 'r') as stopfile:
            stopwords = stopfile.readlines()
        stopwords = [s.strip() for s in stopwords]
        output = []
        for tup in tops:
            t = tup[0]
            add = True
            for w in t.split(" "):
                if w.lower() in stopwords:
                    add = False
            if add:
                output.append(t)
        return output

    #Step 2 - double API step. keywords -> set of song lyrics
    def songLyrics(filepath, keywords):
        rawSongs = musixmatch.get_all_songs(keywords) #musixmatch first
        print "\n\nRAW SONGS from MUSIXMATCH: ", len(rawSongs)

        songs = genius.get_all_songs(rawSongs)
        print "\n\nGENIUS GET", len(songs)

        lyricsDict = lyric_scraper.get_lyrics(songs, filepath.split(".")[0])
        print "\n\nLYRICS DICT FROM GENIUS..."
        return lyricsDict

    #Step 3 - word model step using NGrams
    # def getTopSongs(filepath, lyricsDict):
    #     print "\n\nCALCULATING C-E WITH ORIGINAL TEXT..."
    #     corpus = Corpus(filepath, casefold=True)
    #     wordmodel = NGram(1, 'word', 0.8, openvocab=False)
    #     ts = corpus.tokenized_sents
    #     wordmodel.estimate_from_text(ts)
    #     enum = lyricsDict.items()
    #     #song is (id, [title by, lyrics, url])
    #     entropies = []
    #     for song in enum:
    #         lyrics = song[1][1]
    #         titleBy = song[1][0]
    #         ce = wordmodel.cross_entropy(lyrics.split())
    #         entropies.append((titleBy, ce))
    #     ranked = sorted(entropies,key=itemgetter(1))
    #     return ranked

    rawtext = open(filepath).read().decode('unicode_escape').encode('ascii','ignore')
    print "RAKE....."
    kws = extractKeywords(rawtext)
    print "Proper nouns...."
    pns = properNouns(rawtext)
    fkws = kws + pns
    noDups = list(set([i.lower() for i in fkws]))
    print "WITHOUT DUPLICATES: ", noDups
    print "ALL KEYWORDS/PROPER NOUNS GATHERED: ", fkws
    print "Lyrics...."
    lyrics = songLyrics(filepath, kws)
    print "Cross-entropy...."
    return getTopSongs(filepath, lyrics)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("datadir", help="directory where dataset is located", type=str)
    args = parser.parse_args()
    start_time = time.time()
    results = main(args.datadir)
    print results, '\n\n'
    print("--- %s seconds ---" % (time.time() - start_time))
