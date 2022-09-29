import requestHandler
import fylke
import coordinates

def get_code_muni_basic(muni_nr):
    return requestHandler.get_json_code("https://ws.geonorge.no/kommuneinfo/v1/kommuner/" + str(muni_nr))

def get_code_stedsnavn_kommune(name, muni_nr):
    return requestHandler.get_json_code("https://ws.geonorge.no/stedsnavn/v1/sted?sok=" + name + "&fuzzy=false&knr=" + str(muni_nr) + "&navneobjekttype=kommune&utkoordsys=4258&treffPerSide=10&side=1")

def get_code_stedsnavn_tettsted(name, muni_nr):
    return requestHandler.get_json_code("https://ws.geonorge.no/stedsnavn/v1/sted?sok=" + name + "&fuzzy=false&knr=" + str(muni_nr) + "&navneobjekttype=by&navneobjekttype=tettsted&navneobjekttype=bygdelagBygd&utkoordsys=4258&treffPerSide=10&side=1")

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

def get_coord_long(code_stedsnavn):
    return coordinates.convert_coordinates(code_stedsnavn["navn"][0]["representasjonspunkt"]["øst"])

def get_coord_lat(code_stedsnavn):
    return coordinates.convert_coordinates(code_stedsnavn["navn"][0]["representasjonspunkt"]["nord"])