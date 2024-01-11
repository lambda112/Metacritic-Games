import requests as r
from selectolax.parser import HTMLParser

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
resp = r.get("https://www.metacritic.com/browse/game/", headers=headers)
tree = HTMLParser(resp.content)



