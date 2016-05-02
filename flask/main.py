from flask import Flask, render_template, request
from fullSkeleton import *
import soundcloud
import requests

app = Flask(__name__)

def display_songs(track_urls):
    output = ""
    # create a client object with your app credentials
    client = soundcloud.Client(client_id='11e23e1c664965e66bc2fde70d37a9c2')
    track_urls = list(set(track_urls)) #remove duplicates
    for u in track_urls:
        try:
            embed_info = client.get('/oembed', url=u)
            output = output + embed_info.html
        except requests.exceptions.HTTPError, err:
            print "+ Soundcloud embed error for ", u
            continue
    return output

@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('f2.html')
    elif request.method == 'POST':
        #[('full', u'hi')]
        items = request.form.items()
        print items
        if items[0][0] == "full":
            print "-----------> using full text option..."
            req = request.form["full"]
            urls = bookbeats(req.split(" ")[0], req) #req is the full text, in this case, take the 1st word from a next text as its "title "
            return render_template('f2.html', word = request.form["full"], results = display_songs(urls))
        x = -1
        if items[0][0] == "word":
            print "---------> got title"
            req = request.form["word"] #this is the book title
            urls = bookbeats(req, "builtin") #do the whole entire thing
            return render_template('f2.html', word = request.form["word"], results = display_songs(urls))

if __name__ == '__main__':
    app.run(debug=True)
