import requestHandler
from urllib.parse import quote


def get_list(place_name):
    place_name = place_name.replace(" ", "+")
    url = "https://persondata.toolforge.org/index.php?geb_ort=" + quote(place_name) + "&export=1&format=wiki"

    try:
        code = requestHandler.get_html_code(url)

        code = code.replace(" norwegischer ", " ")
        code = code.replace(" norwegische ", " ")
    except:
        print ("exception")
        code = ""

    return code
