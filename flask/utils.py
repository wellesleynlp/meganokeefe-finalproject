from __future__ import division  # floating point division
from math import log
from collections import Counter
import random

__author__='Sravana Reddy'

def normalize(countdict):
    """given a dictionary mapping items to counts,
    return a dictionary mapping items to their normalized (relative) counts
    Example: normalize({'a': 2, 'b': 1, 'c': 1}) -> {'a': 0.5, 'b': 0.25, 'c': 0.25}
    """
    total = sum(countdict.values())
    return {item: val/total for item, val in countdict.items()}

def basic_count(itemlist):
    """return a dictionary of item counts in a sequence of items
    Example: basic_count('abac') -> {'a': 2, 'b': 1, 'c': 1}
    basic_count(['the', 'hat', 'in', 'the', 'hat']) -> {'the': 2, 'hat': 2, 'in': 1}
    """
    return dict(Counter(itemlist))

def length_count(itemlist):
    """return a dictionary mapping each length value to
    the count of items of that length
    Example: length_count(['the', 'last', 'year']) -> {3: 1, 4: 2}
    """
    return dict(Counter(map(len, itemlist)))  # transform itemlist to list of lengths, and take counts

def expectation(dist):
    """from a dictionary mapping numerical items to relative counts,
    compute and return the weighted average value
    (i.e., if dist represents a random variable, return the expectation)
    Example: expectation({1: 0.5, 2: 0.25, 3: 0.25}) -> 1.75
    """
    return sum([l*c for (l, c) in dist.items()])

def entropy(probdist):
    """given a dictionary mapping items to probabilities,
    return the entropy of the probability distribution in bits
    Example: entropy({'a': 0.5, 'c': 0.5}) -> 1.0
    entropy({'a': 0.5, 'c': 0.25, 'b': 0.25}) -> 1.5
    entropy({'a': 0.5, 'c': 0.25, 'b': 0.25', 'd': 0.0}) -> 1.5
    """
    return sum([-p*log(p, 2) for p in probdist.values() if p>0])

def sample_from_dist(d):
    """given a dictionary representing a discrete probability distribution
    (keys are atomic outcomes, values are probabilities)
    sample a key according to the distribution.
    Example: if d is {'H': 0.7, 'T': 0.3}, 'H' should be returned about 0.7 of time.
    """
    roll = random.random()
    cumul = 0
    for k in d:
        cumul += d[k]
        if roll < cumul:
            return k

def tuple_count(itemlist, tuplen):
    """return a dictionary of tuple counts,
    where each tuple is a subsequence of length tuplen,
    from a sequence of items
    Example: tuple_count('mississippi', 3) -> {('i', 's', 's'): 2, ('m', 'i', 's'): 1, ('s', 'i', 's'): 1,
    ('s', 's', 'i'): 2, ('i', 'p', 'p'): 1, ('p', 'p', 'i'): 1, ('s', 'i', 'p'): 1}
    tuple_count(['the', 'hat', 'in', 'the', 'hat'], 2) -> {('hat', 'in'): 1, ('the', 'hat'): 2, ('in', 'the'): 1}
    """
    counts = {}
    for i in range(1, len(itemlist)+1):
        if i-tuplen >= 0:
            tup = tuple(itemlist[i-tuplen:i])
            counts[tup] = counts.get(tup, 0) + 1
    return counts