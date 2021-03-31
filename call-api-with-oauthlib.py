from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("USERNAME")
if username == None:
	sys.exit("[!] Username not set")

password = os.getenv("PASSWORD")
if password == None:
	sys.exit("[!] Password not set")

url = "https://www.thegazette.co.uk/oauth/token"
scope = "trust"
basic_token = "Basic dHNvOkphdmEkY3IxcHQh"


client = LegacyApplicationClient(client_id=basic_token, scope=scope)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=url, username=username, password=password,
		include_client_id=True)
