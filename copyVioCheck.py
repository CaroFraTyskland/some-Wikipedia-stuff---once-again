import requestHandler

#returns the article with the most likely violation
def get_possible_violation(article):
    URL = ("https://copyvios.toolforge.org/api.json?lang=de&project=wikipedia&title="+ str(article) +"&action=search&use_engine=1&use_links=1&turnitin=1&format=json")
    result = requestHandler.get_json_code(URL)

    bestURL = result["best"]["url"]
    bestConfidence = result["best"]["confidence"]

    print (str(bestURL) + ": " + str(bestConfidence))