import requests
import json

class Repository:

	base_url = "https://api.github.com/"

	headers = { "Accept": "application/vnd.github.v3+json",
				"Content-Type": "application/json; charset=utf-8"
				}


	def __init__(self, username, password):
	
		self.username = username
		self.password = password



	def list_repositories(self):

		url = Repository.base_url + "user/repos"

		username = self.username

		password = self.password

		parameters = {"sort": "updated" }

		response = requests.request("GET", url, headers=Repository.headers, params=parameters, auth=(username, password))

		array = json.loads(response.text)

		for item in array:
			for key, value in item.items():
				if key == "name":
					print(value)



	def create_repository(self, name):

		url = Repository.base_url + "user/repos"

		username = self.username

		password = self.password

		data = json.dumps({ "name": name })

		response = requests.request("POST", url, headers=Repository.headers, data = data, auth=(username, password))

		if response.status_code == 201:
			print("Success!")
			print(response.text)
		else:
			print(response.text)



	def delete_repository(self, name):

		url = Repository.base_url + "repos/firozhc/"+str(name)

		username = self.username

		password = self.password

		response = requests.request("DELETE", url, headers=Repository.headers, auth=(username, password))

		if response.status_code == 204:
			print("Success!")
		else:
			print(response.text)


