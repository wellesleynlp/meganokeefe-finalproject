#Full skeleton: given a single input text file, return top songs
#created 4/1

import argparse
import time
import pprint as pp
from os import listdir
from os.path import isfile, join
import rake
import musixmatch
import lyric_scraper
import operator
import random


def main(filepath):
    #Step 1- RAKE. returns a list of keyword phrases from the input text.
    def extractKeywords(filepath):
        rawtext = open(filepath).read()
        #rawtext = rawtext.decode("string_escape")
        #rawtext = rawtext.decode('utf-8')
        rake_object = rake.Rake("SmartStoplist.txt", 3, 2, 3)
        #each word has at least _ chars; each phrase has at most _ words, each keyword appears at least _ times.
        keywords = rake_object.run(rawtext)
        top = keywords[:15]
        #randomSample = [ keywords[i] for i in sorted(random.sample(xrange(len(keywords)), 15)) ]
        #just get the keywords themselves
        output = [item[0] for item in top]
        return output

    #Step 2 - API step. keywords -> set of song lyrics
    def songLyrics(filepath, keywords):
        songs = musixmatch.get_all_songs(keywords)
        lyricsDict = lyric_scraper.get_lyrics(songs)
        return lyricsDict

    #Step 3 - word model step using NGrams
    def getTopSongs(lyrics):
        return []

    kws = extractKeywords(filepath)
    lyrics = songLyrics(filepath, kws)
    return lyrics
    #return getTopSongs(lyrics)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("datadir", help="directory where dataset is located", type=str)
    args = parser.parse_args()
    start_time = time.time()
    results = main(args.datadir)
    print results, '\n\n'
    print("--- %s seconds ---" % (time.time() - start_time))
