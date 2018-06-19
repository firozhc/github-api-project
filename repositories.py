import requests
import json

def list_repositories(username, password):

	url = "https://api.github.com/users/firozhc/repos"

	headers = { "Accept": "application/vnd.github.v3+json",
				"Content-Type": "application/json; charset=utf-8"
			  }

	parameters = { "visibility": "private", "sort": "updated" }

	r = requests.request("GET", url, headers=headers, params=parameters, 
							auth=(username, password))

	array = json.loads(r.text)

	for item in array:
		for key, value in item.items():
			if key == "name":
				print(value)




def create_repository(username, password):

	url = "https://api.github.com/user/repos"

	headers = { "Accept": "application/vnd.github.v3+json",
				"Content-Type": "application/json; charset=utf-8"
			  }

	data = json.dumps({ "name": "Hello-World4"})

	r = requests.request("POST", url, headers=headers, data = data,  
							auth=(username, password))

	if r.status_code == 201:
		print("Success!")
	else:
		print(r.text)


def main():

	base_url = "https://api.github.com/users/firozhc"
	username = "emperorscourge@gmail.com"
	password = "Apple_123"

	create_repository(username, password)

	list_repositories(username, password)

if __name__=="__main__":
	main()
	
	
