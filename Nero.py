import urllib.request
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import requests
import re

Game_Name, Game_ID, Is_Free, Dev, Pub, Price, W, M, L, Meta, Cat, Gen, Reco = [],[],[],[],[],[],[],[],[],[],[],[],[]
Eng, Ger,Ara,Tur,Fre,Spa, Gre, Rus, Ita, Kor, Jap, Por, Cze, Dan, Dut, Fin, Hun, Nor, Pol, Rom, Chi, Swe, Tha, Bul, Ukr = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
Action, Adventure, Casual, Indie, MassivelyMultiplayer, Racing, RPG, Simulation, Sports, Strategy  = [],[],[],[],[],[],[],[],[],[]
positive = []
#for loop to extract all game info in that range of IDs
for id in range(236849, 236871):
    res = urllib.request.urlopen("https://store.steampowered.com/api/appdetails/?appids="+str(id)+"&l=english&cc=us")
    jj = json.load(res)
    resp = requests.get("https://store.steampowered.com/api/appdetails/?appids="+str(id)+"&l=english&cc=us")
    html = resp.text

    temp = jj[str(id)]
    if temp["success"]:
        temp = temp["data"]
        
        if temp["type"] == "game": #checks if the ID belongs to a game or not
            
            #gives the name of the game
            if "name" in temp:
                game_name = temp["name"]
                print(game_name)
                Game_Name.append(game_name)
            else:
                print("None")
                
            #gives the ID of the game
            if "steam_appid" in temp:
                game_id = temp["steam_appid"]
                print(game_id)
                Game_ID.append(game_id)
            else:
                print("None")
                
            #tells if the game is free or not            
            if "is_free" in temp:
                is_free = temp["is_free"]
                
            else:
                is_free = "Is Free option not given"
                
            print(is_free) 
            Is_Free.append(is_free)
            
            #gives the suppoted languages for the game            
            if "supported_languages" in temp: 
                supported_languages = temp["supported_languages"]
                if "English" in supported_languages:
                    English = 1
                else:
                    English = 0
                Eng.append(English)
                
            
            #gives the name of the developers
            if "developers" in temp:
                for i in range (0,len(temp["developers"])):
                    developer = (temp["developers"])[i]
                                          
            else:
                developer = "Developer info not found"
                
            print(developer)
            Dev.append(developer)
            
            #gives the name of the publishers
            if "publishers" in temp:
                for i in range (0,len(temp["publishers"])):
                    publisher = (temp["publishers"])[i]
                    
            else:
                publisher = "Publisher info not found"
                
            print(publisher)
            Pub.append(publisher)
            
            #gives the price of the game if it exists, if it is not gives "None"
            if "price_overview" in temp :
                price = (temp["price_overview"])["final_formatted"]  
                
            else:
                price = "Not given"
                
            print(price)   
            Price.append(price)
            
            #gives the supported PC platforms as True or False   
            windows =  (temp["platforms"])["windows"]
            print(windows)
            W.append(windows)
            
            mac = (temp["platforms"])["mac"]
            print(mac)
            M.append(mac)
            
            linux = (temp["platforms"])["linux"]
            print(linux)
            L.append(linux)
            
            #gives the Metacritic score of the game if it exists
            if "metacritic" in temp :
                metacritic_score = (temp["metacritic"])["score"] 
                
            else:
                metacritic_score = "Metacritic score not found"
            
            print(metacritic_score)
            Meta.append(metacritic_score)
            
            #gives the categories defined by Steam for the game    
            if "categories" in temp:

                for i in range (0,len(temp["categories"])):
                    categorie = temp["categories"][i]
                   
            else:
                categorie = "Categorie info not found"
            print(categorie)    
            Cat.append(categorie)
            
            #gives the genres defined by Steam for the game
            if "genres" in temp:

                for i in game_id :
                    genre = temp["genres"]
                    genres = pd.DataFrame(genre)
                    genreList = genres["description"].tolist()

                    if genreList[i] == "Action" :
                        act = 1
                    else :
                        act = 0


                            if  "Action" in genreList :
                                act = 1
                            else :
                                act = 0
                            Action.append(act)

                            if "Strategy" in genreList :
                                stra = 1
                            else :
                                stra = 0
                            Strategy.append(stra)

                            if "Adventure" in genreList :
                                adv = 1
                            else :
                                adv = 0
                            Adventure.append(adv)

                            if "Casual" in genreList :
                                cas = 1
                            else :
                                cas = 0
                            Casual.append(cas)

                            if "Indie" in genreList :
                                ind = 1
                            else :
                                ind = 0
                            Indie.append(ind)

                            if "Massively Multiplayer" in genreList :
                                mmult = 1
                            else :
                                mmult = 0
                            MassivelyMultiplayer.append(mmult)

                            if "Racing" in genreList :
                                rac = 1
                            else :
                                rac = 0
                            Racing.append(rac)

                            if "RPG" in genreList :
                                rpg = 1
                            else :
                                rpg = 0
                            RPG.append(rpg)

                            if "Simulation" in genreList :
                                sim = 1
                            else :
                                sim = 0
                            Simulation.append(sim)

                            if "Sports" in genreList :
                                spr = 1
                            else :
                                spr = 0
                            Sports.append(spr)



            else:
                genre ="Genre info not found"
            print(genre)
            Gen.append(genre)
            
            #gives the recommendation number for the game    
            if "recommendations" in temp:
                recommendation_number = (temp["recommendations"])["total"]
                
            else:
                recommendation_number = "Recommendation number is not found"
            print(recommendation_number)
            Reco.append(recommendation_number)
            
            #positive_review = re.findall("class='game_review_summary positive' "(.*?)%", html)
            #positive_review = re.findall("class='game_review_summary positive' r"[0-9][0-9]%"", html)
            #positive.append(positive_review)
            

keys = ["Game_Name","Game_ID","Is_Free","English","Developers","Publishers","Price","Windows","Mac","Linux","Metacritic","Categories","Action", "Strategy", "Adventure", "Indie", "Massively Multiplayer", "Racing", "RPG", "Simulation", "Sports","Recommendation_Number"]

games_data = []
for i in range(0,len(Game_Name)):
    games_dict = dict(zip(keys, [Game_Name[i], Game_ID[i],Is_Free[i], Eng[i], Dev[i], Pub[i], Price[i], W[i], M[i], L[i], Meta[i], Cat[i], Action[i], Strategy[i], Adventure[i], Indie[i], MassivelyMultiplayer[i], Racing[i], RPG[i], Simulation[i], Sports[i], Reco[i]]))

    games_data.append(games_dict)
    
Data_Prep = pd.DataFrame(games_data)
print(Data_Prep.Simulation)