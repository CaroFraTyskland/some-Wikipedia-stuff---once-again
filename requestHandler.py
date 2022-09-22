import requests
import urllib.request


#retrieves data from a given url and returns it
def get_json_code(URL):
    response = requests.get(URL, timeout=0.5)

    return response.json()

#retrieves html from a given url and returns it
def get_html_code(URL):
    fp = urllib.request.urlopen(URL)
    html = fp.read().decode("utf8")
    fp.close()

    return html

#retrieves html from a given url and returns it
def get_html_code_without_head(URL):
    html = get_html_code(URL)

    index = html.index("</head>") + 7
    html = html[index:]

    return html