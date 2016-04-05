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
