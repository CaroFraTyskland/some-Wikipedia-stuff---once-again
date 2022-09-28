import requestHandler
import fylke

def get_code_muni_basic(municipality_number):
    return requestHandler.get_json_code("https://ws.geonorge.no/kommuneinfo/v1/kommuner/" + str(municipality_number))

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