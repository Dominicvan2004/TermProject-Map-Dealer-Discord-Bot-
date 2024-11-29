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
def get_responses(user_input: str) -> str:
  lowered: str = user_input.lower()
  
  

 # f'https://osu.ppy.sh/beatmapsets/{randint(1,1075607)}#osu/{randint(1,2250670)}'
  # This checks for a specific response and if the response matches "mapplz" it returns a random beatmap


  beatmap = client.get_beatmapset(4635746)
  if lowered == "mapplz":
    return beatmap