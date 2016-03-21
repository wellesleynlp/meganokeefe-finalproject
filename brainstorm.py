#Brainstorming the Bookbeats algorithm
#last update: 3/21

import rake_test
import requests

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
request = "https://api.genius.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=REQUESTED_SCOPE&state=SOME_STATE_VALUE&response_type=code"



#STEP 3: FOR EACH SONG COMPUTE CROSS-ENTROPY BETWEEN INITIAL TEXT

#STEP 4: RETURN THE TOP 8 SONGS
