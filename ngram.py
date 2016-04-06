from __future__ import division  # floating point division
from math import log

from utils import *

from collections import Counter, defaultdict

__author__='Your name here'

class NGram:
    """Class for estimating and applying n-gram probabilities from a corpus.
    """
    def __init__(self, n, unit, lam, openvocab=True):
        """Initialize an n-gram model over the level of words or characters (as specified by unit).
        'lam' is the linear interpolation factor:
        P(x|m length context) = lam*relative-count(x|m-length context) + (1-lam)*P(x|m-1 length context)
        'openvocab' is a boolean that specifies whether this model should handle out of vocabulary items
        (items not seen in training data).
        """
        self.n = n
        self.unit = unit
        self.lam = lam  # not calling it "lambda" because of name conflicts
        self.openvocab = openvocab   # true of false: is this model open vocabulary?

        # set up the relative counts dictionary
        self.relcounts = {}
        for i in range(n):
            # conditional probability dictionary for i+1 grams
            self.relcounts[i] = defaultdict(lambda : defaultdict(float))

        self.vocabulary = set()   # vocabulary of items - empty set

    def unigram_entropy(self):
        """return entropy of this model's unigram MLE distribution, in bits"""
        return entropy(self.relcounts[0][()])

    def __str__(self):
        """string representation of this object"""
        return '{0}-gram model over {1}s with linear interpolation factor of {2:.2f}'.format(self.n, self.unit, self.lam)

    def generate(self, numunits):
        """print a list of random sentences, totaling numunits,
        by sampling from this model (no smoothing).
        Use this method to visualize the model, or for fun.
        """
        cursent = []
        if self.n > 1:
            cursent.append('<s>')

        wordcount = 0
        while wordcount < numunits:
            if len(cursent) < self.n:  # sample from lower order distribution
                context = tuple(cursent)
                word = sample_from_dist(self.relcounts[len(cursent)][context])
            else:
                if self.n == 1:
                    context = ()
                else:
                    context = tuple(cursent[-self.n+1:])
                word = sample_from_dist(self.relcounts[self.n-1][context])

            if word == '</s>': # print this sentence, and start a new one
                if self.unit == 'character':
                    print ''.join(cursent[1:])
                else:
                    print ' '.join(cursent[1:])
                cursent = ['<s>']

            else:
                if word != '<s>':
                    wordcount += 1

                if word != '<s>' or cursent == []:
                    cursent.append(word)

        # print final sentence
        if len(cursent)>1:
            if self.unit == 'character':
                print ''.join(cursent[1:])
            else:
                print ' '.join(cursent[1:])


	#HELPER for estimate_from_text (preps traindata + builds the vocabulary)
    def build_vocab(self, traindata):
        seen = [] #used when openvocab = true, to track unknowns
        for scount, sentence in enumerate(traindata):
            for wcount, word in enumerate(sentence):
        		if not word in seen:
        			seen.append(word)
        			if self.openvocab:
        				traindata[scount][wcount] = "<UNK>"
        			else:
        				self.vocabulary.add(word) #closed vocab = add no matter what
        		else:
        			self.vocabulary.add(word) #redundant for charmodel.
        for s in traindata:
        	s.insert(0, "<s>")
        	s.append("</s>")
        self.vocabulary.add("<s>")
        self.vocabulary.add("</s>")
        return traindata

    def getAllTuples(self, updated):
        alltuples = {}
        for sentence in updated: #avoid ngrams spanning sentences
            for key, value in tuple_all_lengths_count(sentence, self.n).iteritems():
                if key in alltuples:
                    alltuples[key] = alltuples[key] + value
                else:
                    alltuples[key] = value
        return alltuples

    # section (a) starts here
    def estimate_from_text(self, traindata):
        """Estimate the parameters (self.relcounts) of this model given a list of sentences,
        where each sentence is a list of words.

        If self.openvocab is true, model should also handle potential "out of vocabulary" item:
        replace the first occurrence of every word type in traindata with <UNK>,
        and train as usual.

        The model should add <s> and </s> tags to the beginning and end of each sentence before
        estimation. (Watch out for how you handle this with character models.)

        Add every item seen in traindata (other than <UNK>) to self.vocabulary.
        """

         # add tokens to self.vocab, replace first occurences with <UNK> when necessary
        tokensSeen = set()
        if self.unit == 'character':
            for sentence in traindata:
                chars = []
                for unit in sentence:
                    chars = chars + list(unit) + [" "]
                chars.pop()
                traindata[traindata.index(sentence)] = chars

        for sentence in traindata:
            for i,unit in enumerate(sentence):
                unitSeen = unit not in self.vocabulary
                # when in character mode, split and combine characters from sentence words
                if self.openvocab:
                    if unitSeen:
                        if unit not in self.vocabulary:
                            self.vocabulary.add(unit)
                    else:
                        tokensSeen.add(unit)
                        sentence[i] = "<UNK>"
                else:
                    if unit not in self.vocabulary:
                            self.vocabulary.add(unit)

            traindata[traindata.index(sentence)].append("</s>")
            traindata[traindata.index(sentence)].insert(0, "<s>")
        self.vocabulary.add("<s>")
        self.vocabulary.add("</s>")



        # tuple_count for each order and combine counts into one list
        tupledData = {}
        #print "Before tupling", traindata
        for sentence in traindata:
            tupled = tuple_all_lengths_count(sentence, self.n)
            for item in tupled:
                if item in tupledData:
                    tupledData[item] += tupled[item]
                else:
                    tupledData[item] = tupled[item]

        # sort tupleData into relcounts
        for item in tupledData:
            order = len(item)-1
            prefix = item[0:order]
            follow = item[len(item)-1]
            self.relcounts[order][prefix][follow] = tupledData[item]

        # normalize tuple counts in each key of each order of relcounts
        for order in self.relcounts:
            for prefix in self.relcounts[order]:
                self.relcounts[order][prefix] = normalize(self.relcounts[order][prefix])

    '''    #*********** DATA PREP ************************************************
        if self.unit=='character':
        #*********** DATA PREP ************************************************
        if self.unit=='character':
        	traindata = splitChar(traindata) #method beneath tuple-all-lengths
        updated = self.build_vocab(traindata)
        #print "\n updated traindata:\n", updated

        #*********** UNIGRAMS RELCOUNTS ****************************************
        alltuples = self.getAllTuples(updated)
        #treating unigrams as a special case - add to relcounts separately
        unigrams = dict((k, v) for k, v in alltuples.iteritems() if len(k)==1)
        self.relcounts[0] = {(): normalize(unigrams)}
        #keep track of the previous ngrams dictionary (which for bigrams, is unigrams)
        prev = dict((k, v) for k, v in unigrams.iteritems())

        #*********** NGRAMS RELCOUNTS ****************************************
        if self.n > 1:
            for g in range (1, self.n): #g = 1 => bigrams, 2 => trigrams....
                ngrams = dict((k, v) for k, v in alltuples.iteritems() if len(k)==g+1)
                table = {} #empty out table from last time
                for prefix, count in prev.iteritems(): #prefix -> row header. eg. ('a', 'a')
                    row = {}
                    #get all appropriately-sized grams that start with this prefix
                    startswith = dict((k, v) for k, v in ngrams.iteritems() if k[0:g]==prefix)
                    for k, v in startswith.iteritems(): #populate the row with counts
                        row[k[g]] = v
                    if row: #this excludes empty rows - hopefully this is fine.
                        table[prefix] = normalize(row)

                self.relcounts[g] = table #insert this table into relcounts
                prev = ngrams #gear up for next iteration

=======
                self.relcounts[g] = table #insert this table into relcounts
                prev = ngrams #gear up for next iteration '''

    def get_prob(self, x, context):
        """return probability(x|context) using linear interpolation,
        where context is a list of items.
        If self.openvocab is True and x or any of the context items are not in self.vocabulary,
        replace them by <UNK>.
        """
        order = len(context)
        if self.openvocab:
            for word in context:
                if word not in self.vocabulary:
                    context[context.index(word)] = "<UNK>"
            if x not in self.vocabulary:
                x = "<UNK>"
        if self.relcounts[order].get(tuple(context), {}) != {}:
            first = self.relcounts[order][tuple(context)].get(x,0)
        else:
            first = 0
        if order >= 1:
            second = self.get_prob(x, context[1:])
        else:
            second = self.relcounts[0][()].get(x, 0)

        return self.lam*first + (1-self.lam)*second


    def cross_entropy(self, text):
        """return the cross entropy in bits of this n-gram model on
        text, which is a list of units (words or characters),
        adding <s> and </s> tags as described in class (EVEN FOR UNIGRAMS according to A2)
        """
        temp = text[:]
        temp.insert(0, "<s>")
        temp.append("</s>")
        diff = 0
        #print "\nCross entropy for: ", temp, " + now iterating on words..."
        for i, x in enumerate(temp):
            #print "i = ", i, "x = ", x, ". "
            if i < self.n: #base case #1: we must take a reduced context
                context = temp[0:i]
                #print "\n\n*** i IS LESS than self.n, context is now ", context, "*****\n\n"
            else:
                context = temp[i-self.n+1:i]
                #print "no reduced context needed, context = ", context, ". "
            #print "RELCOUNTS: ", self.relcounts
            #print "\n\n\n ----- self.get_prob(", x, ",", context, ") = ", self.get_prob(x, context), "----------------\n\n\n"
            value = self.get_prob(x, context)
            if value > 0:
                diff = diff - log(self.get_prob(x, context), 2)
        return diff / len(temp) #divide by 8



def tuple_all_lengths_count(itemlist, maxlen):
    """similarly to utils.tuple_count,
    return a dictionary of tuple counts from a sequence of items
    where each tuple is a subsequence of length ranging from 1 through maxlen.
    Make a single linear pass through the sequence to collect these counts.
    """
    tuples = {}
    for i in range(1, maxlen + 1):
      tuples.update(tuple_count(itemlist, i))
    return tuples

def splitChar(original):
	""" Given a list of sentences, each element of which is a word, return a list of sentences
	where each element is a char (includes whitespace)
	"""
	output = []
	for sentence in original:
		insert = []
		for word in sentence:
			insert = insert + list(word) + [' ']
		insert.pop() #remove trailing space from end of sentence
		output.append(insert)
	return output
