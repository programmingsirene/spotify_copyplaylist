## SPOTIFY API - CREATE NEW PLAYLIST FOR  MISSED HITS ##

### FILL YOUR OWN ####
spotify_user_id = ""
missed_hits_id = ""

# imports
from refresh import Refresh
import json
import requests
from datetime import date

class saveSongs:
	##### FUNCTION ######
	####  initialize
	def __init__(self):
		self.user_id = spotify_user_id
		self.spotify_token = ""
		self.missed_hits_id = missed_hits_id
		self.tracks = ""
		self.new_playlist_id = ""

	#### FUNCTION ####
	#### collect songs from missed hits
	def find_songs(self):
		print("\nCollecting songs from missed hits...\n")

		query = "https://api.spotify.com/v1/playlists/{}/tracks".format(missed_hits_id)

		# request
		response = requests.get(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

		# response
		response_json = response.json()
		
		# print code - is it working 200 OK
		# print(response)

		# create list of tracks
		for i in response_json["items"]:
			self.tracks += (i["track"]["uri"] + ",")
		self.tracks = self.tracks[:-1]

		# function call to add songs to playlist
		self.add_to_playlist()
		
		# print(i["track"]["uri"])

		# can verify with a print
		# print(self.tracks)

	#### FUNCTION ####
	#### create playlist
	def create_playlist(self):
		print("\nCreating new playlist...\n")

		today = date.today()
		today_formatted = today.strftime('%m/%d/%Y')

		# declarations
		query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)

		# request create playlist
		request_body = json.dumps({"name": today_formatted + " missed hits", "description": "Missed hits playlist collecting on this playlist", "public": True})

		# response - post - create playlist
		response = requests.post(query, data=request_body, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

		response_json = response.json()
		# print(response_json)

		# save playlist id
		return response_json["id"]

	#### FUNCTION ####
	#### add songs to new playlist
	def add_to_playlist(self):

		self.new_playlist_id = self.create_playlist()

		print("\nAdding missed hits to new playlist...\n")

		#print(self.tracks)

		query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.new_playlist_id, self.tracks)

		response = requests.post(query, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.spotify_token)})

		# print(response.json)

	#### FUNCTION CALL ####
	def call_refresh(self):
		print("Refreshing token...")
		refresh_caller = Refresh()
		self.spotify_token = refresh_caller.refresh()
		
		# call find_songs
		self.find_songs()

###
# run it
a = saveSongs()
a.call_refresh()
print("\nPlaylist created!\n")
# end
