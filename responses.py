from random import choice, randint

def get_responses(user_input: str) -> str:
  lowered: str = user_input.lower()

  if lowered == '':
    return 'Noting dear'
  elif 'hello' in lowered:
    return 'Hello there'


    
  