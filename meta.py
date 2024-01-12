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


# Create Pandas DataFrame
def create_table():
    data = {
        "Name": all_names,
        "Rating": all_ratings,
        "Description": all_descriptions
    }

    game_info = pd.DataFrame(data).set_index("Name")
    return game_info.to_excel("MetaCritic.xlsx")


all_names = []
all_ratings = []
all_descriptions = []

for i in range(1,545):
    
    print(f"PAGE {i}")
    sleep(1)

    # Parse HTML
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    resp = r.get(f"https://www.metacritic.com/browse/game/?releaseYearMin=1958&releaseYearMax=2024&page={i}", headers=headers)
    tree = HTMLParser(resp.content)

    # Extend each list with previous page games info
    all_names.extend(get_game_names())
    all_ratings.extend(get_game_rating())
    all_descriptions.extend(get_game_description())


create_table()






