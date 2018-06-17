import requests
import json


def authenticate(url):
	r = requests.request("GET", url)
	print(r.text)
	

def main():
	base_url = "https://api.github.com"
	authenticate(url)

if __name__=="__main__":
	main()
	
	
