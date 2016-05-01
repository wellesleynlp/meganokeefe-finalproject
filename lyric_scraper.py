from urlparse import urljoin
from bs4 import BeautifulSoup
import requests
import pprint as pp
import os

#Web scraper for Genius (subverts API)
def get_lyrics(input, title):
    if not os.path.exists(title):
        os.makedirs(title)
    output = {}
    count = 1
    for s in input:
        url = s[2]
        print count, ": scraping... ", url
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        soup = BeautifulSoup(response.text, "lxml")
        lyrics = soup.find('div', class_='song_body-lyrics').text.strip()
        output[s[1]] = [s[0], lyrics, s[2]]
        #write to txtfile
        with open(title+"/"+str(count)+".txt", "wb") as outfile:
            outfile.write(lyrics.encode('utf8'))
            outfile.close()
        count = count + 1
    return output
