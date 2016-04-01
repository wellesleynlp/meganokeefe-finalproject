#Experimenting with RAKE keyword extractor
#https://www.airpair.com/nlp/keyword-extraction-tutorial
#Megan, 3/21/16

import rake
import operator

def get_keywords(text, minChars, mostWords, wordAppears):
    #Rake uses modifiable parameters
    rake_object = rake.Rake("SmartStoplist.txt", minChars, mostWords, wordAppears)
    #each word has at least 5 chars; each phrase has at most 3 words, each keyword appears at least 4x.
    keywords = rake_object.run(text)
    return keywords
