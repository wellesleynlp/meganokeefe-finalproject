#Brainstorming the Bookbeats algorithm
#last update: 3/21

import rake_test
import genius

#THE INPUT TEXT
filename = 'carroll-alice.txt' #(this will be an arg)
input = open(filename).read()

#STEP 1: EXTRACT A LIST OF KEYWORDS FROM TEXT
allKeywords = rake_test.getKeywords(filename)
#keywords is a list of tuples. extract the top 25 for now
topTen = allKeywords[:25]
tk = [item[0] for item in topTen]
print "\nTOP KEYWORDS FOR", filename, ": ", tk, "\n"

#(another tool to look at - Topia TermExtract )

#STEP 2: QUERY GENIUS FOR EACH KEYWORD -> SET OF CANDIDATE SONGS + LYRICS
#code in genius.py
print "\nQUERYING GENIUS API.....\n"
allSongs = []
for kw in tk:
    allSongs = allSongs + genius.get_songs(kw)

#with open('songsout.txt', 'w') as outfile:
#    outfile.write(allSongs)

#STEP 3: FOR EACH SONG COMPUTE CROSS-ENTROPY BETWEEN INITIAL TEXT

#STEP 4: RETURN THE TOP 8 SONGS
