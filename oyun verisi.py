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
                print(game_name)
                Game_Name.append(game_name)
            else:
                print("None")

            # gives the ID of the game
            if "steam_appid" in temp:
                game_id = temp["steam_appid"]
                print(game_id)
                Game_ID.append(game_id)
            else:
                print("None")

            # tells if the game is free or not
            if "is_free" in temp:
                is_free = temp["is_free"]

            else:
                is_free = "Is Free option not given"

            print(is_free)
            Is_Free.append(is_free)

            # gives the suppoted languages for the game
            if "supported_languages" in temp:
                supported_languages = temp["supported_languages"]
                sl = supported_languages.split(",")
                if "English" in sl:
                    sl1 = "English"
                if "German" in sl:
                    sl2 = "German"
                if "French" in sl:
                    sl3 = "French"
                if "Spanish" in sl:
                    sl4 = "Spanish"
                if "Italian" in sl:
                    sl5 = "Italian"
                for i in range(1, 6):
                    print(sl[i])


            else:
                sl = "Language info not found"

            print(sl)
            Lang.append(sl)

            # gives the name of the developers
            if "developers" in temp:
                for i in range(0, len(temp["developers"])):
                    developer = (temp["developers"])[i]

            else:
                developer = "Developer info not found"

            print(developer)
            Dev.append(developer)

            # gives the name of the publishers
            if "publishers" in temp:
                for i in range(0, len(temp["publishers"])):
                    publisher = (temp["publishers"])[i]

            else:
                publisher = "Publisher info not found"

            print(publisher)
            Pub.append(publisher)

            # gives the price of the game if it exists, if it is not gives "None"
            if "price_overview" in temp:
                price = (temp["price_overview"])["final_formatted"]

            else:
                price = "Not given"

            print(price)
            Price.append(price)

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
                metacritic_score = "Metacritic score not found"

            print(metacritic_score)
            Meta.append(metacritic_score)

            # gives the categories defined by Steam for the game
            if "categories" in temp:
                for i in range(0, len(temp["categories"])):
                    categorie = (temp["categories"])[i]

            else:
                categorie = "Categorie info not found"
            print(categorie)
            Cat.append(categorie)

            # gives the genres defined by Steam for the game
            if "genres" in temp:
                for i in range(0, len(temp["genres"])):
                    genre = temp["genres"][i]

            else:
                genre = "Genre info not found"
            print(genre)
            Gen.append(genre)

            # gives the recommendation number for the game
            if "recommendations" in temp:
                recommendation_number = (temp["recommendations"])["total"]

            else:
                recommendation_number = "Recommendation number is not found"
            print(recommendation_number)
            Reco.append(recommendation_number)

            # positive_review = re.findall("class='game_review_summary positive' "(.*?)%", html)
            # positive_review = re.findall("class='game_review_summary positive' r"[0-9][0-9]%"", html)
            # positive.append(positive_review)

keys = ["Game_Name", "Game_ID", "Is_Free", "Supported_Languages", "Developers", "Publishers", "Price", "Windows", "Mac",
        "Linux", "Metacritic", "Categories", "Genres", "Recommendation_Number"]

games_data = []
for i in range(0, len(Game_Name)):
    games_dict = dict(zip(keys,
                          [Game_Name[i], Game_ID[i], Is_Free[i], Lang[i], Dev[i], Pub[i], Price[i], W[i], M[i], L[i],
                           Meta[i], Cat[i], Gen[i], Reco[i]]))

    games_data.append(games_dict)

Data_Prep = pd.DataFrame(games_data)
print(Data_Prep)