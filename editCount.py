import requestHandler


def get_edit_count(user):
    url = "https://de.wikipedia.org/w/api.php?action=query&list=users&ususers=" + user + "&usprop=editcount&format=json"

    response = requestHandler.get_json_code(url)

    try:
        return response["query"]["users"][0]["editcount"]
    except:
        return 0


def print_edit_count(user):
    ec = get_edit_count(user)
    ec = "{:,}".format(ec)
    print(ec.replace(",", "."))
