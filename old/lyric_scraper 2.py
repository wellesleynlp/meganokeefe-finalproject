#updated song lyric scraper
#4/3/16

import requests
import pprint as pp
import json

#id, name, artist
def get_lyrics(songID):
    baseUrl = "http://api.musixmatch.com/ws/1.1/"
    key = "565ef6135740029f3ca72cd7abd59f20"
    query = "track.lyrics.get?track_id=" + songID
    url = baseUrl + query + "&apikey=" + key
    print url
    #url = baseUrl + query + "&apikey=" + key
    #r = requests.get(url)
    #results = r.json()
