import requests

#retrieves data from a given url and returns it
def get_json_code(URL):
    response = requests.get(URL, timeout=0.5)

    return response.json()