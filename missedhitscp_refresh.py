#### REFRESHES ACCESS TOKEN ####
import requests
import json

#### FILL YOUR OWN ####
refresh_token = ""
base_64 = ""

# definition
class Refresh:

	def __init__(self):
		self.refresh_token = refresh_token
		self.base_64 = base_64

	def refresh(self):

		query = "https://accounts.spotify.com/api/token"

		response = requests.post(query, data={"grant_type": "refresh_token","refresh_token": refresh_token}, headers={"Authorization": "Basic " + base_64})

		response_json = response.json()

		# print(response.json())

		return response_json["access_token"]


# end

# test run
# a = Refresh()
# a.refresh()
