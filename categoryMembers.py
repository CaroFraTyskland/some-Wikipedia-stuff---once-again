import requestHandler

list = []


def __convert_cat_name(cat_name):
    if "Kategorie:" not in cat_name:
        return "Kategorie:" + cat_name

    return cat_name


# puts the articles of the category into a list and if there are subcategories those are checked, too
def __create_article_list(code):
    members = code["query"]["categorymembers"]

    for member in members:
        type = member["type"]
        if type == "page":
            if member["title"] not in list:
                list.append(member["title"])

        elif type == "subcat":
            __check_cat_for_articles(member["title"])


# puts the subcategories of the category into a list and if there are subcategories those are checked, too
def __create_subcat_list(code):
    members = code["query"]["categorymembers"]

    for member in members:
        if member["type"] == "subcat":
            if member["title"] not in list:
                list.append(member["title"])

            __check_cat_for_subcats(member["title"])


def __retrieveCode(cat):
    cat = __convert_cat_name(cat)
    url = "https://de.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=" + str(
        cat) + "&cmlimit=max&cmprop=type|title&format=json"

    return requestHandler.get_json_code(url)


# get the json code and then writes the articles into list
def __check_cat_for_articles(cat):
    code = __retrieveCode(cat)
    __create_article_list(code)


# get the json code and then writes the subcategories into list
def __check_cat_for_subcats(cat):
    code = __retrieveCode(cat)
    __create_subcat_list(code)


# returns a list of articles from a cat
def get_articles_from_list(cat):
    __check_cat_for_articles(cat)

    list.sort()
    return list


# returns a list of subcategories from a cat
def get_subcats_from_list(cat):
    __check_cat_for_subcats(cat)

    return list.sort()


# prints the articles from a cat
def print_articles_cat(cat):
    __check_cat_for_articles(cat)

    list.sort()
    print("\n".join(list))


# prints the subcategories from a cat
def print_subcats_cat(cat):
    __check_cat_for_subcats(cat)

    list.sort()
    print("\n".join(list))
