import time
from random import choice, randint
from dotenv import load_dotenv
from osu import (
    Client,
    BeatmapsetSearchFilter as Filter,
    BeatmapsetSearchStatus as Status,
    BeatmapsetSearchGeneral as General,
    BeatmapsetSearchExtra as Extra,
    BeatmapsetLanguage as Language,
    BeatmapsetGenre as Genre
)
import os

load_dotenv()

client_id = int(os.getenv('CLIENT_ID'))
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = os.getenv('REDIRECT_URL')

client = Client.from_client_credentials(client_id, client_secret, redirect_url)

# This gets the responses within the discord chat log
# def get_responses(user_input: str) -> str:

# #use the search beatmap fucntion to get the url of a ranked beat map 

#     rank_List = [1,2,3,4]
#     lowered: str = user_input.lower()

#     if lowered == "mapplz":
#         while 1:
#             beatmapset = client.get_beatmap(randint(1,3894959))
#             print("test dump")
#             print(beatmapsets)

#             if beatmapset.ranked in rank_List:
#                 return(beatmapset.url)
#                 break


#This reads the chat log and finds the key word "mapplz" then finds a random map via questionably creative method
def get_responses(user_input: str) -> str:
  rank_List = [1,2,3,4]
  lowered: str = user_input.lower()
  if lowered == "mapplz": 
    while 1:
        try:
            newID = randint(1,2289287)
            print(f"This is the idea {newID}")
            beatmapset = client.get_beatmapset(newID)
            time.sleep(1)
            
            print("ranked object:")
            print(beatmapset.ranked)
            if beatmapset.ranked in rank_List:
                return(f"https://osu.ppy.sh/beatmapsets/{newID}")
                break
        except:
            continue
