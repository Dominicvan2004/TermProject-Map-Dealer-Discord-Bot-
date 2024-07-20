client_id = 31073
client_secret = "xbRrvtzuVzD9iVghi8egrOtmBnvjhyR2lTO3FyB0C"

import requests

url = 'https://osu.ppy.sh/oauth/token'
data = 'client_id={}&client_secret={}&grant_type=client_credentials&scope=public'.format(client_id, client_secret)

x = requests.post(url, data = data, headers = {"Accept": "application/json", "Content-Type": 'application/x-www-form-urlencoded'})

print(type(x))
print(x.text)
__bool__(self)