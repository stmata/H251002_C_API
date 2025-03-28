import requests
from icecream import ic

url = 'https://apiweatherrcw2.azurewebsites.net/info'

resp = requests.get(url)
ic(resp.json())