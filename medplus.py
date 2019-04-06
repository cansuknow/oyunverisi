import urllib.request
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import requests
import re

Game_Name, Game_ID, Is_Free, Dev, Pub, Price, W, M, L, Meta, Cat, Gen, Reco = [],[],[],[],[],[],[],[],[],[],[],[],[]
Eng, Ger,Ara,Tur,Fre,Spa, Gre, Rus, Ita, Kor, Jap, Por, Cze, Dan, Dut, Fin, Hun, Nor, Pol, Rom, Chi, Swe, Tha, Bul, Ukr = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
SP, MP, OMP, LMP, COP, OCOP, LCOP, SSS, CPM, PSC, SA, FCS, STC, CA, SW, VR, PAR, SC, VAL, ISS = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]         
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
              
                if "German" in supported_languages:
                    German = 1
                else:
                    German = 0
                Ger.append(German)
            
                if "Arabic" in supported_languages:
                    Arabic = 1
                else:
                    Arabic = 0
                Ara.append(Arabic)
            
                if "Turkish" in supported_languages:
                    Turkish = 1
                else:
                    Turkish = 0
                Tur.append(Turkish)
            
                if "French" in supported_languages:
                    French = 1
                else:
                    French = 0
                Fre.append(French)
            
                if "Spanish" in supported_languages:
                    Spanish = 1
                else:
                    Spanish = 0
                Spa.append(Spanish)
            
                if "Greek" in supported_languages:
                    Greek = 1
                else:
                    Greek = 0
                Gre.append(Greek)                
                      
                if "Russian" in supported_languages:
                    Russian = 1
                else:
                    Russian = 0
                Rus.append(Russian)
            
                if "Italian" in supported_languages:
                    Italian = 1
                else:
                    Italian = 0
                Ita.append(Italian)
            
                if "Korean" in supported_languages:
                    Korean = 1
                else:
                    Korean = 0
                Kor.append(Korean)
            
                if "Japanese" in supported_languages:
                    Japanese = 1
                else:
                    Japanese = 0
                Jap.append(Japanese)
                
                
                if "Portuguese" in supported_languages:
                    Portuguese = 1
                else:
                    Portuguese = 0
                Por.append(Portuguese)
                
                if "Czech" in supported_languages:
                    Czech = 1
                else:
                    Czech = 0
                Cze.append(Czech)
                
                if "Danish" in supported_languages:
                    Danish = 1
                else:
                    Danish = 0
                Dan.append(Danish)
                
                if "Dutch" in supported_languages:
                    Dutch = 1
                else:
                    Dutch = 0
                Dut.append(Dutch)
                
                if "Finnish" in supported_languages:
                    Finnish = 1
                else:
                    Finnish = 0
                Fin.append(Finnish)
                
                if "Hungarian" in supported_languages:
                    Hungarian = 1
                else:
                    Hungarian = 0
                Hun.append(Hungarian)
                
                if "Norwegian" in supported_languages:
                    Norwegian = 1
                else:
                    Norwegian = 0
                Nor.append(Norwegian)
                
                if "Polish" in supported_languages:
                    Polish = 1
                else:
                    Polish = 0
                Pol.append(Polish)
                
                if "Romenian" in supported_languages:
                    Romenian = 1
                else:
                    Romenian = 0
                Rom.append(Polish)
                
                if "Chinese" in supported_languages:
                    Chinese = 1
                else:
                    Chinese = 0
                Chi.append(Chinese)
                
                if "Swedish" in supported_languages:
                    Swedish = 1
                else:
                    Swedish = 0
                Swe.append(Swedish)
                
                if "Thai" in supported_languages:
                    Thai = 1
                else:
                    Thai = 0
                Tha.append(Thai)
                
                if "Bulgarian" in supported_languages:
                    Bulgarian = 1
                else:
                    Bulgarian = 0
                Bul.append(Bulgarian)
                
                if "Ukranian" in supported_languages:
                    Ukranian = 1
                else:
                    Ukranian = 0
                Ukr.append(Ukranian)
                
            
            #gives the name of the developers
            if "developers" in temp:
                developer = temp["developers"]
                for i in range (0,len(developer)):
                    Dev.append(developer)                      
            else:
                developer = "Developer info not found"
                Dev.append(developer)
                
            print(developer)
            
            
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
                
                categorie = temp["categories"]
                categories = pd.DataFrame(categorie)
                catlist = categories["description"].tolist()
                print(catlist)
                if "Single-player" in catlist:
                    sp = 1
                else:
                    sp = 0
                if "Multi-player" in catlist:
                    mp = 1
                else:
                    mp = 0                         
                if "Online Multi-Player" in catlist:
                    omp = 1
                else:
                    omp = 0
                if "Local Multi-Player" in catlist:
                    lmp = 1
                else:
                    lmp = 0
                if "Co-op" in catlist:
                    cop = 1
                else:
                    cop = 0
                if "Online Co-op" in catlist:
                    ocop = 1
                else:
                    ocop = 0
                if "Local Co-op" in catlist:
                    lcop = 1
                else:
                    lcop = 0
                if "Shared/Split Screen" in catlist:
                    sss = 1
                else:
                    sss = 0
                if "Cross-Platform Multiplayer" in catlist:
                    cpm = 1
                else:
                    cpm = 0
                if "Played with Steam Controller" in catlist:
                    psc = 1
                else:
                    psc = 0
                if "Steam Achievements" in catlist:
                    sa = 1
                else:
                    sa = 0
                if "Full controller support" in catlist:
                    fcs = 1
                else:
                    fcs = 0
                if "Steam Trading Cards" in catlist:
                    stc = 1
                else:
                    stc = 0
                if "Captions available" in catlist:
                    ca = 1
                else:
                    ca = 0
                if "Steam Workshop" in catlist:
                    sw = 1
                else:
                    sw = 0
                if "SteamVR Collectibles" in catlist:
                    vr = 1
                else:
                    vr = 0
                if "Partial Controller Support" in catlist:
                    par = 1
                else:
                    par = 0
                if "Steam Cloud" in catlist:
                    sc = 1
                else:
                    sc = 0
                if "Valve Anti-Cheat enabled" in catlist:
                    val = 1
                else:
                    val = 0
                if "Includes Source SDK" in catlist:
                    iss = 1
                else:
                    iss = 0
            
                SP.append(sp)
                MP.append(mp)
                OMP.append(omp)
                LMP.append(lmp)
                COP.append(cop)
                OCOP.append(ocop)
                LCOP.append(lcop)
                SSS.append(sss)
                CPM.append(cpm)
                PSC.append(psc)
                SA.append(sa)
                FCS.append(fcs)
                STC.append(stc)
                CA.append(ca)
                SW.append(sw)
                VR.append(vr)
                PAR.append(par)
                SC.append(sc)
                VAL.append(val)
                ISS.append(iss)
                    
            else:
                categorie = "Categorie info not found"
                
                Cat.append(categorie)
            
            
            
            #gives the genres defined by Steam for the game
            if "genres" in temp:
                genre = temp["genres"]
                genres = pd.DataFrame(genre)
                genreList = genres["description"].tolist()
                print(genreList)
                if "Action" in genreList:
                    act = 1
                else:
                    act = 0
                Action.append(act)

                if "Strategy" in genreList:
                    stra = 1
                else:
                    stra = 0
                Strategy.append(stra)

                if "Adventure" in genreList:
                    adv = 1
                else:
                    adv = 0
                Adventure.append(adv)

                if "Casual" in genreList:
                    cas = 1
                else:
                    cas = 0
                Casual.append(cas)

                if "Indie" in genreList:
                    ind = 1
                else:
                    ind = 0
                Indie.append(ind)

                if "Massively Multiplayer" in genreList:
                    mmult = 1
                else:
                    mmult = 0
                MassivelyMultiplayer.append(mmult)

                if "Racing" in genreList:
                    rac = 1
                else:
                    rac = 0
                Racing.append(rac)

                if "RPG" in genreList:
                    rpg = 1
                else:
                    rpg = 0
                RPG.append(rpg)

                if "Simulation" in genreList:
                    sim = 1
                else:
                    sim = 0
                Simulation.append(sim)

                if "Sports" in genreList:
                    spr = 1
                else:
                    spr = 0
                Sports.append(spr)


            else:
                genre = "Genre info not found"
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
            

keys = ["Game_Name","Game_ID","Is_Free",
        "English","German","Arabic","Turkish","French","Spanish",
        "Greek", "Russian","Italian","Korean","Japanese",
        "Portuguese","Czech","Danish",
        "Dutch","Finnish","Hungarian","Norwegian",
        "Polish","Romenian","Chinese","Swedish","Thai","Bulgarian","Ukranian",
        "Developers","Publishers","Price",
        "Windows","Mac","Linux",
        "Metacritic","Single-player","Multi-player","Online Multi-Player",
        "Local Multi-Player", "Co-op","Online Co-op","Local Co-op",
        "Shared/Split Screen","Cross-Platform Multiplayer",
        "Played with Steam Controller","Steam Achievements",
        "Full controller support","Steam Trading Cards","Captions available",
        "Steam Workshop", "SteamVR Collectibles","Partial Controller Support",
        "Steam Cloud","Valve Anti-Cheat enabled","Includes Source SDK",
        "Action", "Strategy", "Adventure", "Indie", "Massively Multiplayer", 
        "Racing", "RPG", "Simulation", "Sports",
        "Recommendation_Number"]

games_data = []
for i in range(0,len(Game_Name)):
    games_dict = dict(zip(keys, [Game_Name[i], Game_ID[i],Is_Free[i], Eng[i], 
                                 Ger[i],Ara[i],Tur[i],Fre[i],Spa[i], Gre[i], 
                                 Rus[i], Ita[i], Kor[i], Jap[i],Por[i], Cze[i], Dan[i], 
                                 Dut[i], Fin[i], Hun[i], Nor[i], Pol[i], Rom[i], Chi[i],
                                 Swe[i], Tha[i], Bul[i], Ukr[i],
                                 Dev[i], Pub[i],Price[i], W[i], M[i], L[i], Meta[i], 
                                 SP[i], MP[i], OMP[i], LMP[i], COP[i], OCOP[i],
                                 LCOP[i], SSS[i],CPM[i], PSC[i], SA[i], FCS[i],
                                 STC[i], CA[i], SW[i], VR[i], PAR[i], SC[i], 
                                 VAL[i], ISS[i], Action[i], Strategy[i], 
                                 Adventure[i], Indie[i], MassivelyMultiplayer[i],
                                 Racing[i], RPG[i], Simulation[i], Sports[i], 
                                 Reco[i]]))

    games_data.append(games_dict)
    
Data_Prep = pd.DataFrame(games_data)
print(Data_Prep)