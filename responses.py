from random import choice, randint

def get_responses(user_input: str) -> str:
  lowered: str = user_input.lower()
  
  if lowered == "mapplz":
    return f'https://osu.ppy.sh/beatmapsets/{randint(1,1075607)}#osu/{randint(1,2250670)}'


    
  