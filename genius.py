import requests
import pprint as pp

def get_songs(kw):
    url = "http://api.genius.com/search?q=" + kw + "&access_token=yAhguhsEC2aduLtKe7C6AwiGJMXVoLvyZIJS1yQMET1ZgzjayNl6gW4lXiEop8gS"
    r = requests.get(url)
    #print r.status_code

    results = r.json()
    #pp.pprint(results)

    songs = results['response']['hits']

    songTitles = []

    for song in songs:
        #title = song['result']['title'].strip()
        #artist = song['result']['primary_artist']['name']
        title = song['result']['full_title']
        songTitles.append(title)
    return songTitles
