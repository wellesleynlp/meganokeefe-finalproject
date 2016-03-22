from urlparse import urljoin
from bs4 import BeautifulSoup
import requests
import pprint as pp

#hacky scrape-y
def get_lyrics(input):
    output = {}
    count = 1
    for s in input:
        url = s[2]
        print count, ": scraping... ", url
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        soup = BeautifulSoup(response.text, "lxml")
        lyrics = soup.find('div', class_='song_body-lyrics').text.strip()
        output[s[1]] = [s[0], lyrics, s[2]]
        count = count + 1
    return output

#list of 3-tuples: (fullTitle, ID, url)
"""input = [(u"Harry Potter and the Philosopher's Stone (Chap. 1 Excerpt) by\xa0J.K.\xa0Rowling", 200832, u'http://genius.com/Jk-rowling-harry-potter-and-the-philosophers-stone-chap-1-excerpt-annotated'), (u'Harry Potter and the Goblet of Fire Script by\xa0Steven\xa0Kloves', 483715, u'http://genius.com/Steven-kloves-harry-potter-and-the-goblet-of-fire-script-annotated'), (u"Harry Potter and the Philosopher's Stone: (Ch. 2) The Vanishing Glass by\xa0J.K.\xa0Rowling", 387797, u'http://genius.com/Jk-rowling-harry-potter-and-the-philosophers-stone-ch-2-the-vanishing-glass-annotated'), (u"Harry Potter and the Philosopher's Stone: (Ch. 3) Letters From No One by\xa0J.K.\xa0Rowling", 396679, u'http://genius.com/Jk-rowling-harry-potter-and-the-philosophers-stone-ch-3-letters-from-no-one-annotated'), (u'Harry Potter and the Deathly Hallows: (Epilogue) Nineteen Years Later by\xa0J.K.\xa0Rowling', 2270198, u'http://genius.com/Jk-rowling-harry-potter-and-the-deathly-hallows-epilogue-nineteen-years-later-annotated'), (u"Harry Potter and the Philosoper's Stone [Ch.5] - Diagon Alley by\xa0J.K.\xa0Rowling", 525795, u'http://genius.com/Jk-rowling-harry-potter-and-the-philosopers-stone-ch5-diagon-alley-annotated'), (u"Harry potter and the sorcerer's stone [chap:7] THE SORTING HAT by\xa0J.K.\xa0Rowling", 710057, u'http://genius.com/Jk-rowling-harry-potter-and-the-sorcerers-stone-chap-7-the-sorting-hat-annotated'), (u'Harry Potter vs. Voldemort Rap by\xa0Indy\xa0Mogul (Ft.\xa0Erik\xa0Beck & Mark\xa0Douglas)', 92406, u'http://genius.com/Indy-mogul-harry-potter-vs-voldemort-rap-lyrics'), (u'Harry Potter flow by\xa0Filipek (Ft.\xa0Feranzo)', 659901, u'http://genius.com/Filipek-harry-potter-flow-lyrics')]
lyricsDict = get_lyrics(input)

with open('hplyrics.txt', 'w') as outfile:
    outfile.write(str(lyricsDict))"""
