import requests

def get_code(article):
    URL = ("https://copyvios.toolforge.org/api.json?lang=de&project=wikipedia&title="+ str(article) +"&action=search&use_engine=1&use_links=1&turnitin=1&format=json")
    response = requests.get(URL)

    return response.json()

#returns the article with the most likely violation
def get_possible_violation(article):
    result = get_code(article)

    bestURL = result["best"]["url"]
    bestConfidence = result["best"]["confidence"]

    print (str(bestURL) + ": " + str(bestConfidence))