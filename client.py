import requests
from icecream import ic

url = 'http://127.0.0.1:8666/info'

resp = requests.get(url)
ic(resp.json())