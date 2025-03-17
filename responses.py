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

#This reads the chat log and finds the key word "mapplz" then finds a random map via questionably creative method
def get_responses(user_input: str) -> str:
  
  lowered: str = user_input.lower()
  beatmapset = client.get_beatmapset(934878)

  if lowered == "mapplz":
    
    while beatmapset.ranked != 1:
            
            try:
                newID = randint(1,100)
                beatmapset = client.get_beatmapset(newID)
            except:
                continue

    return(f"https://osu.ppy.sh/beatmapsets/{newID}")