#!/usr/bin/env python

# system imports
import requests
import json

### youtube variables
youtube_apikey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
youtube_channelname=''

### TVDB variables
tvdb_apikey='XXXXXXXXXXXXXXXX'
tvdb_seriesid=''
language='all'

###################  YOUTUBE  ###################
### Connect to youtube and get the list of videos for a given channel name

## First, from the name, get the playlist ID of all of the uploads for the channel
## For this method, see : http://stackoverflow.com/a/17473477
r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+youtube_channelname+"&key="+youtube_apikey)
j = json.loads(r.text)
playlist_id=j['items'][0]['contentDetails']['relatedPlaylists']['uploads']

## Now we have the playlist_id, get the video details, in pages of 50 at a time
r = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId="+ playlist_id+ "&key="+youtube_apikey)

print r.text

j = r.json()

# If there are more pages of results, loop and ask for each of these in turn
while j.has_key('nextPageToken'):
  next_page_token = j['nextPageToken']
  r = requests.get("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken=" + next_page_token +"&playlistId="+ playlist_id+ "&key="+youtube_apikey)
  j = r.json()
  print next_page_token

print r.text


###################  TVDB  ###################
#####	urllib2.urlopen("http://thetvdb.com/api/" + tvdb_apikey + "/mirrors.xml").read()

#urllib2.urlopen("<mirrorpath_zip>/api/" + tvdb_apikey + "/series/" + tvdb_seriesid + "/all/" + language + ".zip").read()

