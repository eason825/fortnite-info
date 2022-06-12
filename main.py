import requests
import json


api_key = input("Enter Your API KEY: ")
user = input("What user would u like to search for? ")
# you can get an api key by purchasing one here https://boogiefn.sellix.io/ and claiming it in discord.gg/fortnitedev or discord.gg/HfNfDQnPb6


headers = {
  "Authorization": api_key,
  "user": ""
}
r = requests.get("https://api.noteason.xyz/fortnite/public/account/data/user/", headers=headers)
data = r.json()
with open(f'info.json', 'w') as f: 
  json.dump(data, f, indent=3)
print("Data Has Been Dumped Into File Directory info.json")
