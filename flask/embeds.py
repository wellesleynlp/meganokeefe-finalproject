#converting the output playlist into an embeddable list of songs- uses the Soundcloud search API
#5/1/16

import sys
import soundcloud
reload(sys) #deal with Unicode Struggles
sys.setdefaultencoding('utf-8')

def get_urls(raw):
    #raw = [u'A Supermarket in California by\xa0Allen\xa0Ginsberg', u'\xc0s vezes com quem amo by\xa0Marina\xa0Lima', u'Come Alive (feat. Kb, Tedashii, Derek Minor, Andy Mineo, Lecrae & Trip Lee) by\xa0116', u'Ulysses (Chap. 6 - Hades) by\xa0James\xa0Joyce', u'Dragon Fly by\xa0Yann\xa0Tiersen', u'Too Young To Fall In Love by\xa0Chelsea\xa0Lankes', u'Ballad of the Sad Young Men by\xa0David\xa0Sanborn', u"Daddy's Got Your Nose by\xa0The\xa0Paper Chase", u'Young Man by\xa0Styx', u'Young Man by\xa0John\xa0Foxx', u'Open Air by\xa0Lemolo', u'Ballad of the Sad Young Men by\xa0Roberta\xa0Flack', u'All the Young (People of Today) by\xa0Eurythmics', u'Pictures from Italy (Rome) by\xa0Charles\xa0Dickens', u'Western Shore by\xa0Psycho\xa0Motel']

    clean = [r.decode('unicode_escape').encode('ascii','ignore') for r in raw]

    # create a client object with your app credentials
    client = soundcloud.Client(client_id='11e23e1c664965e66bc2fde70d37a9c2')

    urls = []
    for query in clean:
    # find all sounds of buskers licensed under 'creative commons share alike'
        tracks = client.get('/tracks', q=query)
        if len(tracks) > 0:
            urls.append(tracks[0].permalink_url)

    return urls
