import requests
import json

# Get PDF dump using Wikipedia API
def wikipediaRequestArticlePDF(title):
    print("Downloading as PDF...")
    content = requests.get("https://en.wikipedia.org/api/rest_v1/page/pdf/" + title).content
    with open("articles/" + title + ".pdf", "wb") as f:
        f.write(content)

# Get title using Wikidata API
def wikiDataRequestArticles(id):
    print("Requesting " + str(id))
    content = requests.get("https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&props=sitelinks&ids=Q" + str(id) + "&sitefilter=enwiki").content
    jsonObj = json.loads(content)
    try:
        title = jsonObj["entities"]["Q"+str(id)]["sitelinks"]["enwiki"]["title"]
        print("Page found! Title: " + title)
        wikipediaRequestArticlePDF(title)
    except KeyError:
        print(str(id) + " Doesn't exist!")

counter = 1

# Wikidata API IDs are ordered properly, Wikipedia page IDs aren't, so we iterate through Wikidata IDs.

while True:
    wikiDataRequestArticles(counter)
    counter = counter + 1
