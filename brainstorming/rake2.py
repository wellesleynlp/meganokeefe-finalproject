#3/29
#attempt to improve keyword extraction using more books / modified params

import argparse
import time
import pprint as pp
import rake_test
from os import listdir
from os.path import isfile, join

__author__= 'Megan O\'Keefe'



def main(dir):
    def filter(raw):
        final = []
        for k in raw:
            if ' ' in k[0]:
                final.append(k)
        return final

    def callRake(dir):
        mypath = dir
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print files
        minChars = 3
        mostWords = 2
        wordAppears = 1
        books = {}
        for f in files:
            rawtext = open(mypath+f).read().strip()
            print "Getting keywords for ", f
            rawkw = rake_test.get_keywords(rawtext, minChars, mostWords, wordAppears)
            filtered = rawkw
            print filtered
            keywords = [item[0] for item in filtered]
            books[f] = {'keywords': keywords}
        return books
    print "Testing RAKE for ", dir
    callRake(dir)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("datadir", help="directory where dataset is located", type=str)
    args = parser.parse_args()
    start_time = time.time()
    main(args.datadir)
    print("--- %s seconds ---" % (time.time() - start_time))
