import requestHandler
import requests
import re
import categoryMembers

list_ok = ["https://statisticsnorway.shinyapps.io/pendling/", "https://www.ssb.no/statbank/sq/10064050"]


def get_status(url):
    head = requests.head(url)
    return head.status_code


def __extract_urls(article_text):
    article_text = article_text.replace("|Pfad=http", "")  # -{{Webarchiv/Wayback}}
    article_text = article_text.replace("Webarchiv |url=h", "")  # -{{Webarchiv}}

    source_list = re.findall("<ref.*</ref>", article_text)

    # get rid of all web-archive links
    for source in source_list:
        if "web.archive" in source:
            article_text = article_text.replace(source, "")

    article_text = article_text.replace("|archiv-url=http", "")

    return re.findall("(?P<url>https?://[\S]+)", article_text)


def test_article(article_name):
    wiki_url = "https://de.wikipedia.org/w/api.php?action=query&prop=revisions&titles=" + article_name + \
               "&rvslots=%2A&rvprop=content&format=json"

    json = requestHandler.get_json_code(wiki_url)
    content = json["query"]["pages"]

    for key in list(content.keys()):
        print(content[key]["title"] + ":")
        article_text = content[key]["revisions"][0]["slots"]["main"]["*"]

        urls_in_article = __extract_urls(article_text)

        for url in urls_in_article:
            if url not in list_ok:
                status = get_status(url)

                if status != 200:
                    print(url + " " + str(status))
                else:
                    list_ok.append(url)

        print()


def check_category(category):
    articles = categoryMembers.get_articles_from_list(category)

    article_names = ""

    for x in range(len(articles)):

        if x % 10 == 0:
            article_names = articles[x]
        else:
            article_names = article_names + "|" + articles[x]

        if x % 10 == 9:
            test_article(article_names)
            article_names = ""

    if article_names != "":
        test_article(article_names)
