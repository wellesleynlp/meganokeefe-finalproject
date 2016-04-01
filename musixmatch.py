import requests
import pprint as pp
import json

#given a keyword, returns song titles paired with their unique IDs
def get_songs(kw):
    baseUrl = "http://api.musixmatch.com/ws/1.1/"
    key = "565ef6135740029f3ca72cd7abd59f20"
    query = "track.search?q_lyrics=" + kw
    url = baseUrl + query + "&apikey=" + key
    r = requests.get(url)
    results = r.json()
    songs = results['message']['body']['track_list']
    songList = [(song['track']['track_id'], song['track']['track_name'], song['track']['artist_name']) for song in songs]
    return songList

def get_all_songs(kws):
    allSongs = []
    for kw in kws:
        print "MusixMatch API query for ", kw, "..."
        allSongs = allSongs + get_songs(kw)
    return allSongs

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
