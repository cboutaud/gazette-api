from dotenv import load_dotenv
import requests
import os

url = "https://www.thegazette.co.uk/oauth/token"

load_dotenv()
username = os.getenv("USERNAME")
if username == None:
	sys.exit("[!] Username not set")

password = os.getenv("PASSWORD")
if password == None:
	sys.exit("[!] Password not set")

payload = {
	"username": username,
	"password": password,
	"grant_type": "password",
	"scope": "trust"
}

headers = {
	"Authorization": "Basic dHNvOkphdmEkY3IxcHQh"
}

r = requests.post(url, data=payload, headers=headers)

print(r)
print(r.content)
