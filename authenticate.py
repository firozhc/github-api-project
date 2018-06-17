import requests
import json


def authenticate(url):
	username = "emperorscourge@gmail.com"
	password = "Apple_123"

	headers = { "Accept": "application/vnd.github.v3+json", "Content-Type": "application/json; charset=utf-8"}

	r = requests.request("GET", url, headers=headers)
	print(r.text)
	

def main():
	base_url = "https://api.github.com"
	authenticate(base_url)

if __name__=="__main__":
	main()
	
	
