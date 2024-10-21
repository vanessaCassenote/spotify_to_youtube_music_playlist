from ytmusicapi import YTMusic
import json

ytmusic = YTMusic('oauth.json')

def get_songs(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def add_song_to_playlist(playlistId, song):
    
    search_results = ytmusic.search(song)

    if ('videoId' not in search_results[0] or search_results[0]['videoId'] == None):
            for op in search_results:
                if ('videoId' in op and op['videoId'] != None):
                    res = op
                    break
                c += 1
    else:
        res = search_results[0]
    
    ytmusic.add_playlist_items(playlistId, [res['videoId']])
    print(f"The song with ID : {res['videoId']} was added to playlist!")

def find_duplicates(values): 
    duplicates = []
    
    for i, val in enumerate(values):
        if(val in values[i+1:]):
            duplicates.append(val)
    return duplicates
        

def create_playlist(playlist_name, playlist_description, data):
    
    playlistId = ytmusic.create_playlist(playlist_name, playlist_description)
    
    count = 1
    id_songs_list = []
    
    for i in data:
        
        art = ''
        # use only the first 2 artists name, otherwise the search might return empty
        artists = data[i]['artists']
        artists[0:2] if len(artists) > 2 else artists
        
        for a in artists:
            art += ' '+a
        
        song = data[i]['title'] + art
        search_results = ytmusic.search(song)
        
        if ('videoId' not in search_results[0] or search_results[0]['videoId'] == None):
            for op in search_results:
                if ('videoId' in op and op['videoId'] != None):
                    res = op
                    break
        else:
            res = search_results[0]

        id_songs_list.append(res['videoId'])
        ytmusic.add_playlist_items(playlistId, [res['videoId']])
        print(f"----SONG: {song} ADDED----{count}/{len(data)}   id:{res['videoId']}")
        count += 1
    
    print("Adding to playlist.....")
    #ytmusic.add_playlist_items(playlistId, id_songs_list)
    print(f"playlistId : {playlistId}, size : {len(id_songs_list)}")
    
    print(find_duplicates(id_songs_list))
        







if __name__ == "__main__":
    
    filename = "playlist.json"
    playlist_name = "new_playlist"
    playlist_description = "so good"
    
    data = get_songs(filename)
    create_playlist(playlist_name, playlist_description, data)

    # Add one song in a known playlist
    #add_song_to_playlist(playlistId, song='Delicate Taylor Swift')