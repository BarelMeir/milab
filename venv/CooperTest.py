import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
#username = sys.argv[1]
username = 'adwt3hr9ynmjt5cs3ahdcjg63'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
client_id = '57a800c1c950414795bb47f7a4d62281'
client_secret = '9b6842b7cfc54d8f98b9d367b857b01f'
redirect_uri = 'https://www.google.com/'
#Barel User ID: adwt3hr9ynmjt5cs3ahdcjg63
#Barel profile link: adwt3hr9ynmjt5cs3ahdcjg63?si=8leQ4mwHQJCEioQKoSASBw

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri) # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']

# Loop
while True:
    # Main Menu
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")

        # Artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']


        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

    if choice == "1":
        break

    # print(json.dumps(trackResults, sort_keys=True, indent=4))