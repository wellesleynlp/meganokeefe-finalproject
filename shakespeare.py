#Refining keyword extraction using 23 Shakespeare plays as input texts
#Megan, 3/22

from os import listdir
from os.path import isfile, join
import pprint as pp
import rake_test as rt

mypath = "in/will"
infiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

shakes = {}

for f in infiles[1:]:
    print "opening ", f
    raw = open(mypath+"/"+f).read()
    cleaned = raw.split("ACT")[1] #get rid of the license
    bad = ['project', 'gutenberg']
    cleaned = cleaned.split()
    resultwords  = [word for word in cleaned if word.lower() not in bad]
    cleaned = ' '.join(resultwords)
    shakes[f.split('.')[0]] = cleaned

#CLEAN UP / remove licensing



#REFINING KEYWORDS EXTRACTION
macbeth = shakes['king_lear']

minChars = 3
mostWords = 2
wordAppears = 3

keywords = rt.get_keywords(macbeth, minChars, mostWords, wordAppears)
print keywords
