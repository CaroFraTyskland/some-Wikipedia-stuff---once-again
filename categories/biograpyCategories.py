import categoriesFromArticle
import csv
import requestHandler
import time


nations = {}

with open('nationCategories.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        nations["Kategorie:" + row[0]] = 0



url_articles = "https://pageviews.wmcloud.org/userviews/api.php?username=Kenny%20McFly&project=de.wikipedia.org&redirects=0&namespace=0&format=json"

art_response = requestHandler.get_json_code(url_articles)


def update_categories(content):
    try:
        pages = content["query"]["pages"]

        for page_nr in pages:
                    page = pages[str(page_nr)]

                    cats = page["categories"]

                    for cat in cats:
                        if cat["title"] in nations.keys():
                            nations[cat["title"]] += 1
    except:
      print(content)

x = 0

length = len(art_response)

while x < length:   
    articles = []

    max = length
    if (x+15) < max:
       max = x+15

    for s in range(x, max):
        articles.append(art_response[s]["title"])
        print(art_response[s]["title"])

    content = categoriesFromArticle.get_cats_from_articles(articles)

    update_categories(content)

    x = x + 15

print("\n\n")

for k, v in nations.items():
    if v > 0:
        print(k + ": " + str(v))