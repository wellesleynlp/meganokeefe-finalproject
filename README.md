# Bookbeats: Playlist-ify Your Text
Megan O'Keefe, CS349 (Spring 2016)

##Update, 3/29/16
Experimenting with different compiled novel datasets, including:
- (50 books) open source Scifi: https://github.com/alixk/sci_fi
- (441 books) open source English-language novels: https://github.com/JonathanReeve/cenlab

Currently trying to tweak keyword extraction parameters.

Also thinking about how to incorporate randomness into the algorithm- using a random subset of the
top keywords for API querying, for instance. Or, taking a random subset of the top songs.

##Update, 3/22/16

I have written a command-line skeleton of the algorithm (see ce_alice.py) using a combination of existing tools, class code (ngrams and corpus), the Genius API, and a small web scraper. Now my job is to fill out and improve on each of the steps.

**Next steps:**
- Assemble a large set of novels to do tests on
- Refine which keywords should be allowed when querying Genius
- Get better at filtering audio results from Genius

###Step 1: Get an input text (and tokenize/ngram it)
Right now I'm using novels, *Alice in Wonderland* mostly, also *Peter Pan*. The algorithm can be run
on any input text, in theory, but the size of a novel (I hypothesize) makes it more suited for keyword extraction.
Need more texts. Also a larger issue is the NGram model parameters. Currently I'm using unigrams given that
what I'm cross-entropy-ing on is a very small Text B (lyrics to one song). This question will be even more relevant
if I consider allowing smaller input texts (like articles, or poems).

###Step 2: Extract keywords from input text
Right now I'm using an existing Python keyword extraction program, <a href="https://github.com/aneesha/RAKE">RAKE</a>,
described in <a href="http://www.cbs.dtu.dk/courses/introduction_to_systems_biology/chapter1_textmining.pdf">this book chapter</a>.
You can specify how long the keywords can be (ie. words or phrases). Right now I'm getting the top 10 keywords,
mostly due to being scared of overdrawing my API token when I query based on the keywords.

###Step 3: Query Genius API ("Search" feature)
(I do this for the top 10 keywords.) The major problem I'm having is audiobook results (eg. recordings of *Alice*
  for the *Alice* input text), and I'm using crude filtering to get some of those results out.

###Step 4: Get song lyrics for all the songs
The "search" feature doesn't return lyrics, just song metadata. So I have a small web scraper that circumvents the API
temporarily.

###Step 5: Run cross-entropy between song <-> original text
(Then rank them to see which songs have the lowest lyrical cross-entropy.) Audiobook results are again
a major problem here because the lyrics are the actual input text- so it's crucial that I find a way to eliminate these.
