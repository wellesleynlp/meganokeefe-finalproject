#very rough

from ngram import *
from corpus import *
import pprint


filename = "carroll-alice.txt"

corpus = Corpus(filename, casefold=True)

#for now, using unigrams. one song has few words!
wordmodel = NGram(1, 'word', 0.8, openvocab=False)
ts = corpus.tokenized_sents
wordmodel.estimate_from_text(ts)

tayswift = """[Verse 1]
Flashing lights and we
Took a wrong turn and we
Fell down a rabbit hole
You held on tight to me
Cause nothing's as it seems and spinning out of control

[Pre-Chorus 1]
Didn't they tell us don't rush into things?
Didn't you flash your green eyes at me?
Haven't you heard what becomes of curious minds?
Didn't it all seem new and exciting?
I felt your arms twistin' round me
I should have slept with one eye open at night

[Chorus]
We found Wonderland, you and I got lost in it
And we pretended it could last forever
We found Wonderland you and I got lost in it
And life was never worse but never better
In Wonderland
In Wonderland
In Wonderland

[Verse 2]
So we went on our way, too in love to think straight
All alone or so it seemed
But there was strangers watching
And whispers turned to talking
And talking turned to screams, oh

[Pre-Chorus 2]
Didn't they tell us don't rush into things
Didn't you flash your green eyes at me
Didn't you calm my fears with a Cheshire cat smile
Didn't it all feel new and exciting
I felt your arms twisting round me
Its all fun and games till somebody loses their mind

[Chorus]
We found Wonderland, you and I got lost in it
And we pretended it could last forever
We found Wonderland you and I got lost in it
And life was never worse but never better
In Wonderland
In Wonderland
In Wonderland

[Breakdown]
I reached for you but you were gone
I knew I had to go back home
You searched the world for something else
To make you feel like what we had
And in the end, in Wonderland
We both went mad

[Chorus]
We found Wonderland, you and I got lost in it
And we pretended it could last forever
We found Wonderland you and I got lost in it
And life was never worse but never better
In Wonderland
In Wonderland
In Wonderland

[Chorus]
We found Wonderland, you and I got lost in it
And we pretended it could last forever
We found Wonderland you and I got lost in it
And life was never worse but never better
In Wonderland
In Wonderland
In Wonderland"""

julia = """[Verse 1]
I got shit to do
I know you do too
But I won't let go of you
'til you push me away
The second you leave
I miss you
I could see you tomorrow
But I don't wanna wait, so

[Chorus x2]
Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

[Verse 2]
You're an open book
But I can't read you
Start the countdown 'til I lose it
Three, two
One
I'm done, I'm dead
Forget what I said
I'm done, I'm dead
Forget what I said

[Chorus x2]
Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

Oh oh oh oh oh ohoooohoo

[Bridge x2]
I know
What you like so
Baby don't go
Kiss you so slow

[Chorus x2]
Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

Kiss me in the doorway
Always on your way out
I'm trying to make you stay
So we can make out

[Outro]
Oh oh oh oh
Make out
Make out
Make out
Make out"""


ce = wordmodel.cross_entropy(tayswift.split())
print "on TAYLOR SWIFT = ", ce
ce = wordmodel.cross_entropy(julia.split())
print "on JULIA NUNES = ", ce
