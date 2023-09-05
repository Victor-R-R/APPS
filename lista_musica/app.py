import os
from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_id = "c2e052688a31407b93f92bc75b25400e"
client_secret = "2e98795df0e24a2786dd6802864c1f42"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_top_tracks():
    results = sp.search(q='genre:rap genre:hip-hop year:2020-2023', type='track', limit=50)
    tracks = results['tracks']['items']

    top_tracks = []

    for track in tracks:
        top_tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'image_url': track['album']['images'][0]['url'],
            'preview_url': track['preview_url']
        })
    
    return top_tracks

@app.route('/')
def index():
    top_tracks = get_top_tracks()
    return render_template('index.html', tracks=top_tracks)

if __name__ == '__main__':
    app.run(debug=True)