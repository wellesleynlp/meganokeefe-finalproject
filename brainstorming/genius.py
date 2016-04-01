import requests
import pprint as pp
import json

#given a keyword, returns song titles paired with their unique IDs
def get_songs(kw):
    url = "http://api.genius.com/search?q=" + kw + "&access_token=yAhguhsEC2aduLtKe7C6AwiGJMXVoLvyZIJS1yQMET1ZgzjayNl6gW4lXiEop8gS"
    r = requests.get(url)
    results = r.json()
    songs = results['response']['hits']
    songList = [] #list of tuples
    for song in songs:
        #title = song['result']['title'].strip()
        #artist = song['result']['primary_artist']['name']
        title = song['result']['full_title']
        ident = song['result']['id']
        url = song['result']['url']
        if not ('ch.' or 'chap') in title.lower(): #no audiobooks!
            songList.append((title, ident, url))
    return songList

def get_all_songs(kws):
    allSongs = []
    for kw in kws:
        print "API query for ", kw, "..."
        allSongs = allSongs + get_songs(kw)
    return allSongs
