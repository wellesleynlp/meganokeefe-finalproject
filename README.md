# Bookbeats: Playlist-ify Your Text
Megan O'Keefe, CS349 (Spring 2016)

###Update, 4/6/16 (Milestone 1)

My intended first milestone was to have a working command line version of the algorithm, and I have achieved this. The results are lackluster, but the program runs (given an input text, returns a ranked playlist of songs).

I've collapsed all my steps into `fullSkeleton.py`, which leverages other scripts I've written for the API/scraping work (`genius.py, muximatch.py, lyric_scraper.py`). I'm still using the RAKE implementation for my keyword extraction (which I call directly in my extractKeywords function). I'm also using the Corpus and NGram classes that were given to us in the first assignments to do cross-entropy on the original text. 

running `python fullSkeleton.py hamlet.txt` currently outputs the following (the last dictionary has the ranked songs by lowest C-E value with the input text):
	
	MusixMatch API query for  young fortinbras ...
	MusixMatch API query for  lords attendant ...
	MusixMatch API query for  fathers death ...
	MusixMatch API query for  enter polonius ...
	MusixMatch API query for  ile haue ...
	MusixMatch API query for  enter hamlet ...
	MusixMatch API query for  enter horatio ...
	MusixMatch API query for  enter ghost ...
	MusixMatch API query for  good friends ...
	MusixMatch API query for  haue seene ...
	
	
	RAW SONGS from MUSIXMATCH:  32
	Genius query for  (7436530, u'Shakespearean Pie', u'Robert Lund')
	Genius query for  (73153316, u'Faith of Our Fathers', u'Bing Crosby')
	Genius query for  (37836151, u'Faith in Our Fathers', u'Bing Crosby')
	Genius query for  (89226197, u'Faith Of Our Fathers - Single Version', u'Bing Crosby')
	Genius query for  (62192760, u"Let's Die", u'Turbowolf')
	Genius query for  (15825556, u'Scream Aim Fire: The Comics', u'Bullet for My Valentine')
	Genius query for  (18119495, u'My Grandma Was Pearl Hall', u'The Middle East')
	Genius query for  (9564125, u'Eon Aenaos', u'Rotting Christ')
	Genius query for  (1742884, u'Graves of the Fathers', u'Cryptopsy')
	Genius query for  (31253213, u'Pyre of Gods', u'Tarot')
	Genius query for  (50244903, u'Faith of Our Fathers', u'Londonderry Choir')
	Genius query for  (6423689, u"The Poison'd Cup", u'Shakespeare in Hell')
	Genius query for  (84296942, u'Ghost Town', u'Adam Lambert')
	Genius query for  (106588571, u'Ghost Town - Live from Spotify NYC', u'Adam Lambert')
	Genius query for  (83915306, u'Ghost Town (Instrumental Karaoke Version) [In the Style of Adam Lambert]', u'Beat Godz')
	Genius query for  (83583244, u'Interlude; a Ghost in the Wings', u'Crywolf')
	Genius query for  (57024989, u'Canyon City Life', u'The Bullets')
	Genius query for  (2728028, u'(My Heart Is A) Ghost Town', u'Joe Cocker')
	Genius query for  (13549365, u'77(7)', u'@c')
	Genius query for  (94080802, u'Ghost Town - Tribute to Adam Lambert', u'Billboard Masters')
	Genius query for  (84782421, u'Adam Lambert - Ghost Town (GFM Remix)', u'Goblins from Mars')
	Genius query for  (17332330, u'Move It on Over', u'Adam Harvey feat. David Campbell')
	Genius query for  (54787060, u'Good Friends Are for Keeps', u'Carpenters')
	Genius query for  (6656344, u'House Party', u'Nils Landgren Funk Unit')
	Genius query for  (91230401, u'Good Friends', u'Les Thugs')
	Genius query for  (17412918, u'Good Friends and a Bottle of Wine', u'Ted Nugent')
	Genius query for  (68528303, u'Friends', u'Gentle Giant')
	Genius query for  (44247108, u"Here'S To You", u'Peggy Lee')
	Genius query for  (7767221, u'Side Yr On', u'Wavves')
	Genius query for  (18313138, u'My Friends', u'NOFX')
	Genius query for  (55054141, u'Mis Amigos', u'The Dandy Warhols')
	Genius query for  (31538370, u'Afterwards (Bring Yo Friends)', u'Kid Cudi, Michael Bolton & King Chip')
	
	
	GENIUS GET 29
	1 : scraping...  http://genius.com/Robert-lund-shakespearean-pie-lyrics
	2 : scraping...  http://genius.com/Bing-crosby-faith-of-our-fathers-lyrics
	3 : scraping...  http://genius.com/Bing-crosby-faith-in-our-fathers-lyrics
	4 : scraping...  http://genius.com/Bing-crosby-faith-of-our-fathers-single-version-lyrics
	5 : scraping...  http://genius.com/Turbowolf-lets-die-lyrics
	6 : scraping...  http://genius.com/20th-century-fox-deadpool-annotated
	7 : scraping...  http://genius.com/The-middle-east-my-grandma-was-pearl-hall-lyrics
	8 : scraping...  http://genius.com/Rotting-christ-eon-aenaos-lyrics
	9 : scraping...  http://genius.com/Cryptopsy-graves-of-the-fathers-lyrics
	10 : scraping...  http://genius.com/Tarot-pyre-of-gods-lyrics
	11 : scraping...  http://genius.com/James-joyce-ulysses-chap-17-ithaca-annotated
	12 : scraping...  http://genius.com/James-joyce-ulysses-chap-6-hades-annotated
	13 : scraping...  http://genius.com/Adam-lambert-ghost-town-lyrics
	14 : scraping...  http://genius.com/Robert-c-tucker-the-marx-engels-readerchapter-1-annotated
	15 : scraping...  http://genius.com/Lil-yachty-interlude-lyrics
	16 : scraping...  http://genius.com/Cormac-mccarthy-the-road-excerpt-annotated
	17 : scraping...  http://genius.com/Joe-cocker-great-divide-lyrics
	18 : scraping...  http://genius.com/Chief-kamachi-777-lyrics
	19 : scraping...  http://genius.com/James-joyce-finnegans-wake-chap-23-annotated
	20 : scraping...  http://genius.com/Carpenters-good-friends-are-for-keeps-lyrics
	21 : scraping...  http://genius.com/Debbie-sims-sos-lyrics
	22 : scraping...  http://genius.com/Les-thugs-good-friends-lyrics
	23 : scraping...  http://genius.com/Ted-nugent-good-friends-and-a-bottle-of-wine-lyrics
	24 : scraping...  http://genius.com/Gentle-giant-three-friends-lyrics
	25 : scraping...  http://genius.com/Peggy-lee-heres-to-you-lyrics
	26 : scraping...  http://genius.com/Wavves-side-yr-on-lyrics
	27 : scraping...  http://genius.com/Nofx-my-friends-lyrics
	28 : scraping...  http://genius.com/The-dandy-warhols-mis-amigos-lyrics
	29 : scraping...  http://genius.com/Kid-cudi-afterwards-bring-yo-friends-lyrics
	
	
	LYRICS DICT FROM GENIUS...
	
	
	CALCULATING C-E WITH ORIGINAL TEXT...
	[(u"Here's To You by\xa0Peggy\xa0Lee", 2.859689378719101), (u'Graves Of The Fathers by\xa0Cryptopsy', 3.5272087062463924), (u'Deadpool by\xa020th\xa0Century Fox', 3.540401269385299), (u'Ulysses (Chap. 17 - Ithaca) by\xa0James\xa0Joyce', 3.6560129522205953), (u"Finnegan's Wake (Chap. 2.3) by\xa0James\xa0Joyce", 3.7498573288159447), (u'My Grandma Was Pearl Hall by\xa0The\xa0Middle East', 3.9068982593424955), (u'Ulysses (Chap. 6 - Hades) by\xa0James\xa0Joyce', 3.9210704333357707), (u'Faith Of Our Fathers by\xa0Bing\xa0Crosby', 4.069518875820298), (u'Shakespearean Pie by\xa0Robert\xa0Lund', 4.089104638802505), (u'777 by\xa0Chief\xa0Kamachi', 4.1996069902392), (u'Three Friends by\xa0Gentle\xa0Giant', 4.294856612052424), (u'Eon Aenaos by\xa0Rotting\xa0Christ', 4.33043598456477), (u'Faith Of Our Fathers - Single Version by\xa0Bing\xa0Crosby', 4.3344750644719525), (u'Interlude by\xa0Lil\xa0Yachty', 4.357244361980782), (u'Faith in Our Fathers by\xa0Bing\xa0Crosby', 4.474389276422369), (u'Afterwards (Bring Yo Friends) by\xa0Kid\xa0Cudi (Ft.\xa0King\xa0Chip & Michael\xa0Bolton)', 4.591165681364654), (u'The Marx-Engels Reader(Chapter 1) by\xa0Robert\xa0C. Tucker', 4.5956414054567345), (u'Ghost Town by\xa0Adam\xa0Lambert', 4.619630833856085), (u'S.O.S. by\xa0Debbie\xa0Sims', 4.630466584755957), (u'The Road (Excerpt) by\xa0Cormac\xa0McCarthy', 4.894655776836323), (u"Let's Die by\xa0Turbowolf", 5.019713786397761), (u'Great Divide by\xa0Joe\xa0Cocker', 5.26135728592861), (u'Good Friends Are For Keeps by\xa0Carpenters', 5.278250415419262), (u'My Friends by\xa0NOFX', 5.340593017396082), (u'Side yr on by\xa0Wavves', 5.369540873128382), (u'Mis Amigos by\xa0The\xa0Dandy Warhols', 5.530388715352479), (u'Pyre of Gods by\xa0Tarot', 5.57983986740063), (u'Good Friends by\xa0Les\xa0Thugs', 5.629607062039116), (u'Good Friends And A Bottle Of Wine by\xa0Ted\xa0Nugent', 5.6534411101082584)] 
	
	
	--- 34.1735019684 seconds ---


Some problems I'm having: 

1. **Not having enough songs to rank** (Genius and Musixmatch give you up to ten search results, so if I take the top ten keywords, I'll get up to 100 songs, but usually less than this). I've tried to find a legal lyrics database that isn't tokenized or parsed (so that I can do cross-entropy on all the lyrics) and have been unable to.  
2. **Running time** - the original goal of this project was to be able to run it on novels (I also am using some poetry in testing, like *Leaves of Grass*). But right now, running on *Moby Dick* takes well over two minutes to run on my machine. (Is this unavoidable if I want to keep querying these APIs?) 
3. **Mediocre song candidates** due to separately querying on each phrase (is this unavoidable, though?)

With all this in mind, I want to spend the next few weeks continuing to modify my algorithm. Some ideas I have: 

- **To make keyword extraction better**- the RAKE algorithm seems to do its job well on larger texts, but the keywords are sometimes unspecific ("good friends," for example). What if I also added a named entity extraction step, to get place names from the text? I could also write a custom script to parse the most-used words/phrases in "important" parts of the novel (like chapter titles, or the first/last paragraphs).  

- **To figure out a way to get more song lyrics**- my lyric scraper is  not very fast, but it can do as many songs as I want. The bottleneck is with the limits on my Musixmatch token (as well as my Genius API token, which gets the song IDs that the scraper uses in turn). 

- **To fine-tune the cross-entropy step** - it is inevitable that things could be wonky (false positives, etc.) with C-E given that a lyric text is very short, and a novel is very long. The [current top result](http://genius.com/Peggy-lee-heres-to-you-lyrics) for `hamlet.txt` is a song that does not evoke Hamlet. I want to figure out if there's any way this step could be improved to get a more accurate ranking (eg. different NGram parameters?), or if this is just a matter of getting more lyrics). 


###Update, 4/1/16
Updated stopwords so that my keywords aren't people's names (like "Mr. ___") but I might change this as I go. Have experimented with keyword extraction parameters.

I realized that I shouldn't have ever been using Genius to get songs based on keywords, because Genius has annotations for lots of things that aren't songs. This was the problem I was having with getting 'songs' that were actual transcriptions of the input text itself. So I've decided to use the MusixMatch API to get my candidate songs.

Update- Using MusixMatch to get the songs is working a lot better and the queries are also running a lot faster. But the problem is that for lyrics, it only returns 30% of them, meaning that I no longer have a direct link between song information and lyrics. This will be my next task. Hopefully I can find a service that will give me all the lyrics.

###Update, 3/29/16
Experimenting with different compiled novel datasets, including:
- (50 books) open source Scifi: https://github.com/alixk/sci_fi
- (441 books) open source English-language novels: https://github.com/JonathanReeve/cenlab

Currently trying to tweak keyword extraction parameters.

Also thinking about how to incorporate randomness into the algorithm- using a random subset of the
top keywords for API querying, for instance. Or, taking a random subset of the top songs.

###Update, 3/22/16

I have written a command-line skeleton of the algorithm (see ce_alice.py) using a combination of existing tools, class code (ngrams and corpus), the Genius API, and a small web scraper. Now my job is to fill out and improve on each of the steps.

**Next steps:**
- Assemble a large set of novels to do tests on
- Refine which keywords should be allowed when querying Genius
- Get better at filtering audio results from Genius

#####Step 1: Get an input text (and tokenize/ngram it)
Right now I'm using novels, *Alice in Wonderland* mostly, also *Peter Pan*. The algorithm can be run
on any input text, in theory, but the size of a novel (I hypothesize) makes it more suited for keyword extraction.
Need more texts. Also a larger issue is the NGram model parameters. Currently I'm using unigrams given that
what I'm cross-entropy-ing on is a very small Text B (lyrics to one song). This question will be even more relevant
if I consider allowing smaller input texts (like articles, or poems).

#####Step 2: Extract keywords from input text
Right now I'm using an existing Python keyword extraction program, <a href="https://github.com/aneesha/RAKE">RAKE</a>,
described in <a href="http://www.cbs.dtu.dk/courses/introduction_to_systems_biology/chapter1_textmining.pdf">this book chapter</a>.
You can specify how long the keywords can be (ie. words or phrases). Right now I'm getting the top 10 keywords,
mostly due to being scared of overdrawing my API token when I query based on the keywords.

#####Step 3: Query Genius API ("Search" feature)
(I do this for the top 10 keywords.) The major problem I'm having is audiobook results (eg. recordings of *Alice*
  for the *Alice* input text), and I'm using crude filtering to get some of those results out.

#####Step 4: Get song lyrics for all the songs
The "search" feature doesn't return lyrics, just song metadata. So I have a small web scraper that circumvents the API
temporarily.

#####Step 5: Run cross-entropy between song <-> original text
(Then rank them to see which songs have the lowest lyrical cross-entropy.) Audiobook results are again
a major problem here because the lyrics are the actual input text- so it's crucial that I find a way to eliminate these.
