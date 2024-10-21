import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import json

load_dotenv(dotenv_path=".env")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def authenticate():
    # authenticate
    client_credentials_manager = SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )

    # create spotify session object
    session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    return session

def get_playlist_tracks_over_100(session,URI):
    
    results = session.user_playlist_tracks(playlist_id=URI)
    # Get first 100 tracks
    tracks = results['items']
    # keep getting if there is more
    while results['next']:
        results = session.next(results)
        tracks.extend(results['items'])
    
    print(len(tracks))
    return tracks

def get_playlist_tracks_under_100(session,URI):
    
    # get list of tracks in a given playlist (note: max playlist length 100)
    tracks = session.playlist_tracks(URI)["items"]
    return tracks

def save_to_json(playlist_songs, filename):
    with open(filename, "w") as f:
        json.dump(playlist_songs, f)    

def get_playlist(playlist_url):
    
    session = authenticate()

    # Separate the URI of the playlist URL, text between the last '/' and '?'
    URI = playlist_url.rsplit("/",1)[1].split("?",1)[0]
    
    # If you have less than 100 songs, you can use the method below instead   
    #tracks = get_playlist_tracks_under_100(session,URI)

    tracks = get_playlist_tracks_over_100(session,URI)

    playlist_songs = {}
    index = 0
    for track in tracks:
          
        artists = []
        for i in track['track']['artists']:
            artists.append(i['name'])
        
        playlist_songs[index] = {
            'title' : track['track']['name'],
            'artists': artists
        }
        index += 1
    
    return playlist_songs






if __name__ == "__main__":
    
    # playlist URL
    playlist_url = "https://open.spotify.com....."
    filename="playlist.json"
    
    playlist_songs = get_playlist(playlist_url)
    save_to_json(playlist_songs, filename)