This are very simple python scripts to read a playlist from spotify and create it on youtube music.


<b>Spotify</b>
- Create an APP on https://developer.spotify.com/
- use the credential to connect to spotify library (https://spotipy.readthedocs.io/en/2.24.0/)
- copy the URL of your playlist (set 'playlist_url' with it)
- run code with: python spotify_access.py
- a json file with all the songs titles and artists will be created

<b>Youtube Music</b>
- Install ytmusicapi library, follow the steps to autheticate (https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html)
  - run the command: ytmusicapi oauth  (tip: don't forget to click ENTER when the message appear in the command line)
  - a json file called "oauth.json" will be created
  - create a project on google APIs (https://developers.google.com/youtube/v3/guides/auth/devices?hl=pt-br)
- set 'filename' variable with the json file with all songs
- run code with: python youtube_music_access.py   









- References:
https://engineeringfordatascience.com/posts/export_spotify_playlist_to_csv_using_python/
