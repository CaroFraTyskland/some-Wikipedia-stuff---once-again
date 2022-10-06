import requestHandler
import requests
import re

def get_status(url):
    head = requests.head(url)
    return head.status_code

def __extract_urls(article_text):
    article_text.replace("|Pfad=http", "") #-{{Webarchiv/Wayback}}
    
    source_list = re.findall("<ref.*</ref>", article_text)
    
    #get rid of all web-archive links
    for source in source_list:
        if "web.archive" in source:
            article_text = article_text.replace(source, "")
    
    
    article_text.replace("|archiv-url=http", "")
    
    return re.findall("(?P<url>https?://[^\s]+)", article_text)

def test_article(article_name):
    wiki_url = "https://de.wikipedia.org/w/api.php?action=query&prop=revisions&titles=" + article_name + "&rvslots=%2A&rvprop=content&format=json"
    
    json = requestHandler.get_json_code(wiki_url)
    content = json["query"]["pages"]
    
    for key in list(content.keys()):
        print (content[key]["title"] + ":")
        article_text = content[key]["revisions"][0]["slots"]["main"]["*"]
        
        urls_in_article = __extract_urls(article_text)
        
        for url in urls_in_article:
            status = get_status(url)

            if status != 200:
                print(url + " " + str(status))
    