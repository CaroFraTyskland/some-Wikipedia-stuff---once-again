import requestHandler
from urllib.parse import quote

def get_list(place_name):
    place_name = place_name.replace(" ", "+")
    code = requestHandler.get_html_code("https://persondata.toolforge.org/index.php?geb_ort=" + quote(place_name) + "&export=1&format=wiki")
    
    code = code.replace(" norwegischer ", " ")
    code = code.replace(" norwegische ", " ")

    return code