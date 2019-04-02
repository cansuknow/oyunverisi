import urllib.request
import json
import pandas as pd
from pandas.io.json import json_normalize

Game_Name, Game_ID, Is_Free, Supported_Languages, Developers = [], [], [], [], []

# for loop to extract all game info in that range of IDs
for id in range(236849, 236871):
    res = urllib.request.urlopen(
        "https://store.steampowered.com/api/appdetails/?appids=" + str(id) + "&l=english&cc=us")
    jj = json.load(res)


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
                is_free = "Not defined"
                Is_Free.append(is_free)
                print(is_free)

            # gives the suppoted languages for the game
            if "supported_languages" in temp:
                supported_languages = temp["supported_languages"]

            else:
                supported_languages = "Not defined"
            print(supported_languages)
            Supported_Languages.append(supported_languages)
            # gives the name of the developers
            if "developers" in temp:
                for i in range(0, len(temp["developers"])):
                    developer = (temp["developers"])[i]

            else:

                print(developer)

            # gives the name of the publishers
            if "publishers" in temp:
                for i in range(0, len(temp["publishers"])):
                    publisher = (temp["publishers"])[i]
                    print(publisher)
            else:
                print("None")

            # gives the price of the game if it exists, if it is not gives "None"
            if "price_overview" in temp:
                price = (temp["price_overview"])["final_formatted"]
                print(price)
            else:
                print("None")

            # gives the supported PC platforms as True or False
            windows = (temp["platforms"])["windows"]
            print(windows)

            mac = (temp["platforms"])["mac"]
            print(mac)

            linux = (temp["platforms"])["linux"]
            print(linux)

            # gives the Metacritic score of the game if it exists
            if "metacritic" in temp:
                metacritic_score = (temp["metacritic"])["score"]
                print(metacritic_score)
            else:
                print("None")

            # gives the categories defined by Steam for the game
            if "categories" in temp:
                for i in range(0, len(temp["categories"])):
                    categorie = (temp["categories"])[i]
                    print(categorie)
            else:
                print("None")

            # gives the genres defined by Steam for the game
            if "genres" in temp:
                for i in range(0, len(temp["genres"])):
                    genre = temp["genres"][i]
                    print(genre)
            else:
                print("None")

            # gives the recommendation number for the game
            if "recommendations" in temp:
                recommendation_number = (temp["recommendations"])["total"]
                print(recommendation_number)
            else:
                print("None")

keys = ["Game_Name", "Game_ID"]
games_data = []
for i in range(0, len(Game_Name)):
    games_dict = dict(zip(keys, [Game_Name[i], Game_ID[i]]))
    games_data.append(games_dict)


Data_Prep = pd.DataFrame(games_data)
print(Data_Prep)