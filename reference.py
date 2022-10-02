from datetime import datetime

def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d')

def get_source_language():
    return "<ref>{{Internetquelle |url=https://lovdata.no/dokument/SF/forskrift/2019-12-20-2114 |titel=Forskrift om språkvedtak i kommunar og fylkeskommunar (språkvedtaksforskrifta) |werk=Lovdata |sprache=no |abruf=" + get_todays_date() + "}}</ref>"

def get_source_reg_sami():
    return "<ref>{{Internetquelle |url=https://www.regjeringen.no/no/tema/urfolk-og-minoriteter/samepolitikk/samiske-sprak/forvaltningsomradet-for-samisk-sprak/id2910947/ |titel=Forvaltningsområdet for samisk språk |werk=regjeringen.no |sprache=no |datum=2022-04-29 |abruf=" + get_todays_date() + "}}</ref>"

def get_source_reg_reform_2020():
    return "<ref>{{Internetquelle |url=https://www.regjeringen.no/no/tema/kommuner-og-regioner/kommunestruktur/nyekommuneogfylkesnummer/id2629203/ |titel=Nye kommune- og fylkesnummer fra 2020 |werk=regjeringen.no |sprache=no |datum=2020-01-08 |abruf=" + get_todays_date() + "}}</ref>"

def get_source_stadnamn(place_name):
    return "<ref>{{Internetquelle |url= |titel=" + place_name + " |werk=Norsk stadnamnleksikon |abruf=" + get_todays_date() + " |sprache=no}}</ref>"

def get_source_sprakradet():
    return "<ref>{{Internetquelle |url=https://www.sprakradet.no/sprakhjelp/Skriverad/navn-pa-steder-og-personer/Innbyggjarnamn/ |titel=Innbyggjarnamn |werk=Språkrådet |sprache=nn |abruf=" + get_todays_date() + "}}</ref>"

def get_source_ssb_pop_over_time():
    return "<ref>{{Internetquelle |url=https://data.ssb.no/api/v0/dataset/26975.csv?lang=en |titel=Population. Municipalities, pr. 1.1., 1986 - latest year |werk=ssb.no |sprache=en |abruf=" + get_todays_date() + "}}</ref>"

def get_source_ssb_muni_history():
    return "<ref>{{Internetquelle |autor=Dag Juvkam |url=https://www.ssb.no/a/histstat/rapp/rapp_199913.pdf |titel=Historisk oversikt over endringer i kommune- og fylkesinndelingen |werk=Statistisk sentralbyrå |datum=1999 |format=PDF |sprache=no |abruf=" + get_todays_date() + "}}</ref>"

def get_source_highest_mountain():
    return "<ref>{{Internetquelle |url=https://www.kartverket.no/til-lands/fakta-om-norge/hoyeste-fjelltopp-i-kommunen |titel=Høgaste fjelltopp i kvar kommune |hrsg=Kartverket |sprache=nn |abruf=" + get_todays_date() + "}}</ref>"

def get_source_norgeskart(place_name):
    return ("<ref name=\"norgeskart\">{{Internetquelle |url= |titel=" + place_name  + " |werk=Norgeskart |sprache=no |abruf=" + get_todays_date() + "}}</ref>")

def get_snl_url(name):
    name = name.replace(" ", "_")
    return "https://snl.no/" + name

def get_soure_snl(name):
    return "<ref name=\"snl\">{{Internetquelle |autor= |url=" + get_snl_url(name) + " |titel=" + name + " |werk=Store norske leksikon |sprache=no |abruf=" + get_todays_date() + "}}</ref>"

def get_source_ssb_commuter():
    return "<ref>{{Internetquelle |url=https://statisticsnorway.shinyapps.io/pendling/ |titel=Pendlingsstrømmer |hrsg=Statistics Norway |sprache=no |abruf=" + get_todays_date() + "}}</ref>"  

def get_source_ssb_area_type():
    return "<ref>{{Internetquelle |url=https://www.ssb.no/statbank/sq/10064050 |titel=09280: Areal (km²), etter arealtype, statistikkvariabel, år og region |werk=ssb.no |hrsg=Statistisk sentralbyrå |sprache=no |abruf=" + get_todays_date() + "}}</ref>"  
    
def get_snl_weblink(name):
    return "* [" + get_snl_url(name) + " " + name + "] im [[Store norske leksikon]] (norwegisch)"

def get_ssb_muni_weblink(name):
    lowerCaseName = __replace_letters(name.lower()).replace(" ", "-")

    return "* [https://www.ssb.no/kommunefakta/" + lowerCaseName + " Fakten über " + name + "] beim [[Statistisk sentralbyrå]] (norwegisch)"

def __replace_letters(text):
    text = text.replace("Ø", "O")
    text = text.replace("ø", "o")
    text = text.replace("å", "a")
    text = text.replace("Å", "A")
    text = text.replace("æ", "ae")
    text = text.replace("Æ", "Ae")
    text = text.replace("é", "e")
    text = text.replace("è", "e")
    text = text.replace("È", "E")
    text = text.replace("É", "E")

    return text