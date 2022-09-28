import requestHandler
import fylke

def get_code_muni_basic(muni_nr):
    return requestHandler.get_json_code("https://ws.geonorge.no/kommuneinfo/v1/kommuner/" + str(muni_nr))

def get_municipality_name(code_muni_basic):
    return code_muni_basic["kommunenavn"]

def is_samisk_forvaltningsomrade(code_muni_basic):
    return code_muni_basic ["samiskForvaltningsomrade"]

def get_fylke_name(code_muni_basic):
    return code_muni_basic["fylkesnavn"]

def get_fylke_number(code_muni_basic):
    return code_muni_basic["fylkesnummer"]

def get_fylke(code_muni_basic):
    return fylke.get_fylke_by_number(get_fylke_number(code_muni_basic))

def get_neighbour_munis(muni_nr):
    neighbours = []
    code = requestHandler.get_json_code("https://ws.geonorge.no/kommuneinfo/v1/kommuner/"+ str(muni_nr) + "/nabokommuner")

    for muni in code:
        neighbours.append(muni["kommunenummer"])

    return neighbours