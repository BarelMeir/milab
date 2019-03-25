import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import threading

class UserHandler (threading.Thread):
   def __init__(self, userName):
      threading.Thread.__init__(self)
      self.userName = userName
      # Variables to get tracks/artists/albums/genre
      # recentlyPlayedTracksId = []
      self.topTracksId = []
      self.topArtistsId = []
      self.topGenresList = []
      self.sortedGenres = []

   def run(self):
      '''
      coopers cardentials
      client id: '7aa624328ab34962bc800beb9c5e495e'
      client secret: 'cbd7ae1af0994259916b7dd415c9149b'
      redirect: 'http://google.com/'
      '''

      username = self.userName
      scope = 'user-read-recently-played playlist-modify-public user-top-read playlist-read-private playlist-modify-private user-library-read playlist-read-collaborative user-read-private user-follow-read'
      clientID = '7aa624328ab34962bc800beb9c5e495e'
      clientSecret = 'cbd7ae1af0994259916b7dd415c9149b'
      redirectURI = 'http://google.com/'

      # Erase cache and prompt for user permission
      try:
         token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
      except(AttributeError, JSONDecodeError):
         os.remove(f".cache-{username}")
         token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)

      # Create our spotifyObject
      spotifyObject = spotipy.Spotify(auth=token)

      # User information
      user = spotifyObject.current_user()
      displayName = user['display_name']
      print("Hello" + displayName)

      tracksCounter = 0
      artistsCounter = 0
      genresCounter = 0

      # Gets user top tracks
      topTracks = spotifyObject.current_user_top_tracks(50, 0, 'long_term')
      topTracks = topTracks['items']

      # Puts top tracks ids in an array
      for item in topTracks:
         self.topTracksId.append(item['id'])
         tracksCounter += 1

      # Gets users top artist
      topArtists = spotifyObject.current_user_top_artists()
      topArtists = topArtists['items']

      # Puts top artists in an array
      for item in topArtists:
         self.topArtistsId.append(item['id'])
         artistsCounter += 1

      # Gets users top genres
      topGenres = topArtists

      # album find identical variables
      add = True  # If the genre was already added to list - add = false
      genreNumCountList = []  # Counts number of appearance for every genre
      genreNumCounter = 0

      # Puts top genres in an array
      for item in topGenres:  # For every artist
         genres = item['genres']
         for currentGenre in genres:  # Every artist have a few genres
            for genre in self.topGenresList:  # Goes over all the genres we added so far
               if currentGenre == genre:  # If genre is already in the list:
                  add = False  # Don't add it again
                  genreNumCountList[genreNumCounter] += 1  # Count its appearance
                  break
               genreNumCounter += 1
            genreNumCounter = 0
            if add:  # If genre is not in the list
               self.topGenresList.append(currentGenre)  # add it
               genreNumCountList.append(1)  # count appearance
               genresCounter += 1
            add = True

      # Sort genres - most liked - to least liked
      counter = 0
      currentNum = 0
      maxNum = 0

      length = len(genreNumCountList)
      for x in range(0, length):
         for num in genreNumCountList:
            if num > maxNum:
               maxNum = num
               maxNumIndex = counter
            counter += 1
         self.sortedGenres.append(self.topGenresList[maxNumIndex])
         genreNumCountList[maxNumIndex] = -1
         maxNum = 0
         counter = 0
