import requests
import json


def auth(url, username, password):
	
	headers = { "Accept": "application/vnd.github.v3+json",
				"Content-Type": "application/json; charset=utf-8"
			  }

	r = requests.request("GET", url, headers=headers, auth=(username, password))
	
	rjson = json.loads(r.text)

	print(r.headers)

	for key, value in rjson.items():
		print(str(key)+": "+ str(value))
	
	
def main():

	base_url = "https://api.github.com/users/firozhc"
	username = "emperorscourge@gmail.com"
	password = "Apple_123"

	auth(base_url, username, password)

if __name__=="__main__":
	main()
	
	
