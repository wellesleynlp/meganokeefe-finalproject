#Experimenting with RAKE keyword extractor
#https://www.airpair.com/nlp/keyword-extraction-tutorial
#Megan, 3/21/16

import rake
import operator

def get_keywords(filename):
    #Rake uses modifiable parameters
    rake_object = rake.Rake("SmartStoplist.txt", 5, 3, 4)
    #each word has at least 5 chars; each phrase has at most 3 words, each keyword appears at least 4x.
    sample_file = open(filename, 'r')
    text = sample_file.read()
    keywords = rake_object.run(text)
    return keywords
