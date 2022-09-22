import requestHandler

articles = []

def convert_cat_name(cat_name):
    if "Kategorie:" not in cat_name:
        return "Kategorie:" + cat_name

    return cat_name

#puts the articles of the category into a list and if there are subcategories those are checked, too
def create_article_list(code):
    members = code["query"]["categorymembers"]
    print (".")

    for member in members:
        type = member["type"]
        if type == "page":
            if member["title"] not in articles:
                articles.append(member["title"])
        elif type == "subcat":
            check_cat(member["title"])

#get the json code and then writes them into list
def check_cat(cat):
    cat = convert_cat_name(cat)
    url = "https://de.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=" + str(cat) +"&cmlimit=max&cmprop=type|title&format=json"

    response = requestHandler.get_json_code(url)
    create_article_list(response)

#returns a list of articles from a cat
def get_articles_from_list(cat):
    check_cat(cat)
    
    return articles.sort()

#prints the articles from a cat
def print_articles_cat(cat):
    check_cat(cat)

    articles.sort()
    print("\n".join(articles))