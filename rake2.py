#3/29
#attempt to improve keyword extraction using more books / modified params

import pprint as pp
import rake_test
from os import listdir
from os.path import isfile, join

#READ IN FILES
mypath = 'in/small/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#SET UP KEYWORD PARAMS
minChars = 4
mostWords = 2
wordAppears = 15

#ASSEMBLE KEYWORDS: books[name] =
books = {}
for f in files[18:20]:
    rawtext = open(mypath+f).read().strip()
    print "Getting keywords for ", f
    rawkw = rake_test.get_keywords(rawtext, minChars, mostWords, wordAppears)
    filtered = kwfilter.filter()
    print rawkw
    keywords = [item[0] for item in rawkw]
    books[f] = {'keywords': keywords}

#print results
pp.pprint(books)
