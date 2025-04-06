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
