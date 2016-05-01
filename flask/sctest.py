import soundcloud
client = soundcloud.Client(client_id='11e23e1c664965e66bc2fde70d37a9c2')


#STEP 1: GET A SOUNDCLOUD URL BASED ON TITLE, ARTIST
#search?
title = 'Odd'
artist = 'Julia Nunes'
combined = (title + " " + artist).lower()

tracks = client.get('/tracks', q=combined)
top = tracks[0]
track_url = top.permalink_url

#track_url = 'http://soundcloud.com/forss/flickermood'
embed_info = client.get('/oembed', url=track_url)

print embed_info['html']
