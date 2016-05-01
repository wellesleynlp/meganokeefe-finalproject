from flask import Flask, render_template, request
from fullSkeleton import * 
import soundcloud

app = Flask(__name__)

def display_songs(track_urls):
    output = ""
    # create a client object with your app credentials
    client = soundcloud.Client(client_id='11e23e1c664965e66bc2fde70d37a9c2')
    # track_urls = [u'https://soundcloud.com/ginsberg-recordings/a-supermarket-in-california', u'https://soundcloud.com/rapzilla/116-come-alive', u'https://soundcloud.com/dragon-fly-8/cl-mtbd-2ne1-crush', u'https://soundcloud.com/chelsealankes/too-young-to-fall-in-love', u'https://soundcloud.com/dionnefarris/the-ballad-of-the-sad-young', u'https://soundcloud.com/nappyboyofficial/classic-man-feat-vantrease-and-young-cash-tmix', u'https://soundcloud.com/nappyboyofficial/classic-man-feat-vantrease-and-young-cash-tmix', u'https://soundcloud.com/amsterdam-open-air/bakermat-amsterdam-open-air', u'https://soundcloud.com/dionnefarris/the-ballad-of-the-sad-young', u'https://soundcloud.com/purchase-jazz-orchestra/chris-foe-sessions-the-western-shore']
    track_urls = list(set(track_urls)) #remove duplicates
    for u in track_urls:
        embed_info = client.get('/oembed', url=u)
        output = output + embed_info.html
    return output


@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('f2.html')
    elif request.method == 'POST':
        req = request.form["word"] #this is the book title
        urls = bookbeats(req) #do the whole entire thing
        return render_template('f2.html', word = request.form["word"], results = display_songs(urls))


if __name__ == '__main__':
    app.run(debug=True)
