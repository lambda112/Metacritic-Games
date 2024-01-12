import requests as r
import pandas as pd
from time import sleep 
from selectolax.parser import HTMLParser


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


# Get Big Image of Each Game 
def get_game_images():
    image = [i.attrs["src"] for i in tree.css("div > picture > img") if "132" in i.attrs.get("src", "72")] 
    return image


for x in range(1,545):
    
    sleep(1)
    print(f"Page {x}")

    # Parse HTML
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    resp = r.get(f"https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024&page={x}", headers=headers)
    tree = HTMLParser(resp.content)

    # Write to an html file all to get images included 
    game_data = zip(get_game_images(), get_game_names(), get_game_rating(), get_game_description())
    for i in game_data:
        with open("Metacritic.html", "a", encoding = "utf-8") as f:
            f.write(f"<img src = '{i[0]}' alt = '{i[1]}'>")
            f.write(f"<br><p>Game: {i[1]}<br>Rating: {i[2]}<br>Description: {i[3]}<br><br></p>")
            f.write("<hr>")