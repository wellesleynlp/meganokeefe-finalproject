import requests
import pprint as pp
import json

def get_song(kw):
    url = "http://api.genius.com/search?q=" + kw + "&access_token=yAhguhsEC2aduLtKe7C6AwiGJMXVoLvyZIJS1yQMET1ZgzjayNl6gW4lXiEop8gS"
    r = requests.get(url)
    results = r.json()
    songs = results['response']['hits']
    songList = [] #list of tuples
    if len(songs)==0: #no genius hits, too bad.
        return []
    else:
        song = songs[0] #return the top hit
        title = song['result']['full_title']
        ident = song['result']['id']
        url = song['result']['url']
        return (title, ident, url)

def get_all_songs(kws):
    result = []
    for tup in kws:
        tosearch = tup[1] + ' ' tup[2]
        result = result + get_song(tosearch)

kws = [(7436530, u'Shakespearean Pie', u'Robert Lund'), (73153316, u'Faith of Our Fathers', u'Bing Crosby'), (37836151, u'Faith in Our Fathers', u'Bing Crosby'), (89226197, u'Faith Of Our Fathers - Single Version', u'Bing Crosby'), (62192760, u"Let's Die", u'Turbowolf'), (15825556, u'Scream Aim Fire: The Comics', u'Bullet for My Valentine'), (18119495, u'My Grandma Was Pearl Hall', u'The Middle East'), (1742884, u'Graves of the Fathers', u'Cryptopsy'), (9564125, u'Eon Aenaos', u'Rotting Christ'), (31253213, u'Pyre of Gods', u'Tarot'), (62966456, u'Vinland', u'Unleashed'), (6423689, u"The Poison'd Cup", u'Shakespeare in Hell'), (84296942, u'Ghost Town', u'Adam Lambert'), (106588571, u'Ghost Town - Live from Spotify NYC', u'Adam Lambert'), (83915306, u'Ghost Town (Instrumental Karaoke Version) [In the Style of Adam Lambert]', u'Beat Godz'), (83583244, u'Interlude; a Ghost in the Wings', u'Crywolf'), (57024989, u'Canyon City Life', u'The Bullets'), (2728028, u'(My Heart Is A) Ghost Town', u'Joe Cocker'), (13549365, u'77(7)', u'@c'), (94080802, u'Ghost Town - Tribute to Adam Lambert', u'Billboard Masters'), (84782421, u'Adam Lambert - Ghost Town (GFM Remix)', u'Goblins from Mars'), (17332330, u'Move It on Over', u'Adam Harvey feat. David Campbell'), (54787060, u'Good Friends Are for Keeps', u'Carpenters'), (6656344, u'House Party', u'Nils Landgren Funk Unit'), (91230401, u'Good Friends', u'Les Thugs'), (17412918, u'Good Friends and a Bottle of Wine', u'Ted Nugent'), (68528303, u'Friends', u'Gentle Giant'), (44247108, u"Here'S To You", u'Peggy Lee'), (7767221, u'Side Yr On', u'Wavves'), (18313138, u'My Friends', u'NOFX'), (55054141, u'Mis Amigos', u'The Dandy Warhols'), (31538370, u'Afterwards (Bring Yo Friends)', u'Kid Cudi, Michael Bolton & King Chip'), (7436530, u'Shakespearean Pie', u'Robert Lund'), (18722927, u'Combat Jack Show Freestyle', u'Heems'), (1909219, u'The Vibes', u'Beastie Boys'), (70558858, u'4 Life', u"Dj Myst feat. Alivor, Lentyss & Sam's"), (925855, u'The Nang, the Front, the Bush and the Shit', u'El-P'), (7947723, u"O'or Hamlet", u'Brobdingnagian Bards'), (88774546, u'The Vibes - 2009 Digital Remaster', u'Beastie Boys'), (15331720, u'Sweetest Love', u'Katherine Jenkins'), (19687538, u'Simple Gifts', u'Yo-Yo Ma & Alison Krauss'), (96457699, u'Simple Gifts', u'All Angels'), (89218534, u'For Boston', u'Dropkick Murphys'), (50321510, u'Gift to Be Simple', u"The King's Singers"), (98789867, u'Stricken, Smitten and Afflicted', u'Fernando Ortega'), (19586019, u'Si\xfail, a R\xfain', u'Anuna'), (3048990, u'Simple Gifts', u'Judy Collins'), (42389641, u'Beautiful Stranger', u'Briana Evigan & Kevin "Ogre" Ogilvie'), (81813995, u'The Dog and Her Reflection / Beautiful Stranger', u'Briana Evigan feat. Terrance Zdunich'), (5694771, u'Celia', u'Enigma'), (35653028, u'Keep the Faith, Baby', u'Tony Bennett & k.d. lang'), (1804684, u'Leap of Faith', u'Etta James'), (4583114, u'Magnify the Lord', u'Kurt Carr & The Kurt Carr Singers'), (34874847, u'Oh Magnify the Lord', u'Kurt Carr & The Kurt Carr Singers'), (86322534, u'Good Life Remix', u'Faith Evans feat. Ja Rule, Vita & Caddillac Tah'), (15366681, u'Good Life (Special mix)', u'Faith Evans feat. Ja Rule & Vita'), (80706697, u'Ever Had a Little Faith?', u'Belle and Sebastian'), (33607222, u'Keeping the Faith', u'Javen'), (80786431, u'(Baby) Make Me Feel So Good', u'The Five Stairsteps'), (48665736, u'Faith In the Devil', u'Wednesday 13')]
print get_all_songs(kws):
