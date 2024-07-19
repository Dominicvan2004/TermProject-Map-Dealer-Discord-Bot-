from random import choice, randint
# This gets the responses within the discord chat log
def get_responses(user_input: str) -> str:
  lowered: str = user_input.lower()
  
  # This checks for a specific response and if the response matches "mapplz" it returns a random beatmap
  if lowered == "mapplz":
    return f'https://osu.ppy.sh/beatmapsets/{randint(1,1075607)}#osu/{randint(1,2250670)}'


    
  