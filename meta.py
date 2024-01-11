import requests as r
from selectolax.parser import HTMLParser

# Parse HTML
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
resp = r.get("https://www.metacritic.com/browse/game/", headers=headers)
tree = HTMLParser(resp.content)

# Get Name of Each Game
def get_game_names():
    names = [i.text() for i in tree.css("div > h3 > span + span")]   
    return names

# Get Rating of Each Game
def get_game_rating():
    rating = [i.text() for i in tree.css("span div > span")] 
    return rating

# Get Description of Each Game
def get_game_description():
    desc = [i.text().replace("\n", "") for i in tree.css("div[class *= 'desc'] > span")] 
    return desc

print(get_game_description())


