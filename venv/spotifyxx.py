import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username -> qaqknn1mf4oa5ysh7c55rk8wt (Mia Shpan)
username ='qaqknn1mf4oa5ysh7c55rk8wt'
scope = 'user-read-recently-played playlist-modify-public'
clientID = 'f5432fa1ce6543bfa958cd0f83be368d'
clientSecret = 'e019939ff06f4b3d9a57d68e95ada29a'
redirectURI = 'https://google.com/'

# Erase cache and prompt for user permission
try:
    token=util.prompt_for_user_token(username,scope, clientID, clientSecret, redirectURI)
except(AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token=util.prompt_for_user_token(username,scope, clientID, clientSecret, redirectURI)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

# Gets recently played song
recently_played = spotifyObject.current_user_recently_played()
#print(json.dumps(recently_played, sort_keys=True, indent=4))
# Find the band of the song
bandName = recently_played['items'][0]
bandName = bandName['track']['artists'][0]
bandName = bandName['name']

# User information
user=spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

print("HEY " + displayName + "!!")
print()
print("You were recently listening to " + bandName)
print()
print("Lets add a song by " + bandName + " to your playlist")

# Create a new playlist and get playlist ID
spotifyObject.user_playlist_create(username,'cooper',True,'Hey')
playlistID = spotifyObject.current_user_playlists()
playlistID = playlistID['items'][0]
playlistID = playlistID['id']

# Search for the band data
searchResult = spotifyObject.search(bandName,1,0,"artist")

# Artist details
artist = searchResult['artists']['items'][0]
#webbrowser.open(artist['images'][0]['url'])
artistID = artist['id']

# Album and tracks details
trackID = []
z = 0

# extract album data
albumResults = spotifyObject.artist_albums(artistID)
albumResults = albumResults['items']

for item in albumResults:
    print("ALBUM " + item['name'])
    albumID=item['id']

    # Extract track data
    trackResults = spotifyObject.album_tracks(albumID)
    trackResults = trackResults['items']

    for item in trackResults:
        print(str(z) + ": " + item['name'])
        #print(item['id'])
        #print(json.dumps(item, sort_keys=True, indent=4))
        trackID.append(item['id'])
        z+=1
    print

    # add chosen song to playlist
    songSelection = input("Enter a song number to add to your playlist (x to exit)")
    spotifyObject.user_playlist_add_tracks(username,playlistID,[trackID[int(songSelection)]])

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
