import urllib.request
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import requests
import re

Game_Name, Game_ID, Is_Free, Lang, Dev, Pub, Price, W, M, L, Meta, Cat, Gen, Reco = [], [], [], [], [], [], [], [], [], [], [], [], [], []
positive = []
# for loop to extract all game info in that range of IDs
for id in range(236849, 236871):
    res = urllib.request.urlopen(
        "https://store.steampowered.com/api/appdetails/?appids=" + str(id) + "&l=english&cc=us")
    jj = json.load(res)
    resp = requests.get("https://store.steampowered.com/api/appdetails/?appids=" + str(id) + "&l=english&cc=us")
    html = resp.text

    temp = jj[str(id)]
    if temp["success"]:
        temp = temp["data"]

        if temp["type"] == "game":  # checks if the ID belongs to a game or not

            # gives the name of the game
            if "name" in temp:
                game_name = temp["name"]
            else:
                game_name = "Not defined"
            print(game_name)
            Game_Name.append(game_name)

            # gives the ID of the game
            if "steam_appid" in temp:
                game_id = temp["steam_appid"]
            else:
                game_id = "Not defined"
            print(game_id)
            Game_ID.append(game_id)

            # tells if the game is free or not
            if "is_free" in temp:
                is_free = temp["is_free"]
            else:
                is_free = "Not defined"
            print(is_free)
            Is_Free.append(is_free)

            # gives the suppoted languages for the game
            if "supported_languages" in temp:
                supported_languages = temp["supported_languages"]
            else:
                supported_languages = "Not defined"
            print(supported_languages)
            Lang.append(supported_languages)

            # gives the name of the developers
            if "developers" in temp:
                for i in range(0, len(temp["developers"])):
                    developer = (temp["developers"])[i]
            else:
                developer = "Not defined"
            print(developer)
            Dev.append(developer)

            # gives the name of the publishers
            if "publishers" in temp:
                for i in range(0, len(temp["publishers"])):
                    publisher = (temp["publishers"])[i]
            else:
                publisher = "Not defined"
            print(publisher)
            Pub.append(publisher)

            # gives the price of the game if it exists, if it is not gives "None"
            if "price_overview" in temp:
                price = (temp["price_overview"])["final_formatted"]
            else:
                price = "Not defined"
            Price.append(price)
            print(price)

            # gives the supported PC platforms as True or False
            windows = (temp["platforms"])["windows"]
            print(windows)
            W.append(windows)

            mac = (temp["platforms"])["mac"]
            print(mac)
            M.append(mac)

            linux = (temp["platforms"])["linux"]
            print(linux)
            L.append(linux)

            # gives the Metacritic score of the game if it exists
            if "metacritic" in temp:
                metacritic_score = (temp["metacritic"])["score"]
            else:
                metacritic_score = "Not defined"
            Meta.append(metacritic_score)
            print(metacritic_score)

            # gives the categories defined by Steam for the game
            if "categories" in temp:
                for i in range(0, len(temp["categories"])):
                    categorie = (temp["categories"])[i]
            else:
                categorie = "Not defined"
            print(categorie)
            Cat.append(categorie)

            # gives the genres defined by Steam for the game
            if "genres" in temp:
                for i in range(0, len(temp["genres"])):
                    genre = temp["genres"][i]
            else:
                genre = "Not defined"
            print(genre)
            Gen.append(genre)

            # gives the recommendation number for the game
            if "recommendations" in temp:
                recommendation_number = (temp["recommendations"])["total"]
            else:
                recommendation_number = "Not defined"
            print(recommendation_number)
            Reco.append(recommendation_number)

            # positive_review = re.findall("class='game_review_summary positive' r"[0-9][0-9]%"", html)
            # positive.append(positive_review)

keys = ["Game_Name", "Game_ID", "Is_Free","Supported_Languages", "Developers", "Publishers", "Price", "Windows", "Mac", "Linux", "Categories", "Metacritic", "Genres", "Recommendation_Number"]
games_data = []
for i in range(0, len(keys)):
    games_dict = dict(zip(keys,
                          [Game_Name[i], Game_ID[i], Is_Free[i], Lang[i], Dev[i], Pub[i], Price[i], W[i], M[i], L[i], Cat[i], Meta[i], Gen[i], Reco[i]]))
    games_data.append(games_dict)

Data_Prep = pd.DataFrame(games_data)
print(Data_Prep)

