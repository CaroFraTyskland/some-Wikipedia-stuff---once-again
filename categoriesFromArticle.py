import requestHandler

categories = []

#puts the categories of the article into a list
def __create_cat_list(code):
    pages = code["query"]["pages"]

    for page_nr in pages:
        page = pages[str(page_nr)]
        print(page["title"])

        cats = page["categories"]

        for cat in cats:
            categories.append(cat["title"])

#get the json code and then writes the categories into a list
def __check_article(article):
    url = "https://de.wikipedia.org/w/api.php?action=query&prop=categories&titles=" + article + "&cllimit=max&format=json"

    response = requestHandler.get_json_code(url)
    __create_cat_list(response)

#returns a list of categories from an article
def get_cats_from_article(cat):
    __check_article(cat)
    
    return categories.sort()

#prints the categories from an article
def print_cats_from_article(cat):
    __check_article(cat)

    categories.sort()
    print("\n".join(categories))