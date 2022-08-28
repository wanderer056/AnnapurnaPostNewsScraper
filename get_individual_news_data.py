# For individual news data the api link is "https://bg.annapurnapost.com/api/news/{id}"
import json
import requests

f= open('news1.json')

data = json.load(f)

f.close()

id = data[0]["id"]
print()

url = "https://bg.annapurnapost.com/api/news/{}".format(id)

response = requests.get(url)

with open("singlenews.json","w") as outfile:
    outfile.write(response.text)



