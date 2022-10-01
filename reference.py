from datetime import datetime

def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d')

def build_reference(source):
    return "<ref>" + source + "</ref>"

def build_reference_with_name(name, source):
    return "<ref name=\"" + name + "\">" + source + "</ref>"

def get_source_language():
    return "<ref>{{Internetquelle |url=https://lovdata.no/dokument/SF/forskrift/2019-12-20-2114 |titel=Forskrift om språkvedtak i kommunar og fylkeskommunar (språkvedtaksforskrifta) |werk=Lovdata |sprache=no |abruf=" + get_todays_date() + "}}</ref>"

def get_source_reg_sami():
    return "<ref>{{Internetquelle |url=https://www.regjeringen.no/no/tema/urfolk-og-minoriteter/samepolitikk/samiske-sprak/forvaltningsomradet-for-samisk-sprak/id2910947/ |titel=Forvaltningsområdet for samisk språk |werk=regjeringen.no |sprache=no |datum=2022-04-29 |abruf=" + get_todays_date() + "}}</ref>"

def get_source_stadnamn(place_name):
    return "<ref>{{Internetquelle |url= |titel=" + place_name + " |werk=Norsk stadnamnleksikon |abruf=" + get_todays_date() + " |sprache=no}}</ref>"

def get_source_sprakradet():
    return "<ref>{{Internetquelle |url=https://www.sprakradet.no/sprakhjelp/Skriverad/navn-pa-steder-og-personer/Innbyggjarnamn/ |titel=Innbyggjarnamn |werk=Språkrådet |sprache=nn |abruf=" + get_todays_date() + "}}</ref>"

def get_source_ssb_pop_over_time():
    return "<ref>{{Internetquelle |url=https://data.ssb.no/api/v0/dataset/26975.csv?lang=en |titel=Population. Municipalities, pr. 1.1., 1986 - latest year |werk=ssb.no |sprache=en |abruf=" + get_todays_date() + "}}</ref>"

def get_source_norgeskart(place_name):
    return build_reference_with_name("norgeskart", "{{Internetquelle |url= |titel=" + place_name  + " |werk=Norgeskart |sprache=no |abruf=" + get_todays_date() + "}}")

def get_snl_url(name):
    name = name.replace(" ", "_")
    return "https://snl.no/" + name

def get_soure_snl(name):
    return "<ref name=\"snl\">{{Internetquelle |autor= |url=" + get_snl_url(name) + " |titel=" + name + " |werk=Store norske leksikon |sprache=no |abruf=" + get_todays_date() + "}}</ref>"

def get_source_ssb_commuter():
     return "<ref>{{Internetquelle |url=https://statisticsnorway.shinyapps.io/pendling/ |titel=Pendlingsstrømmer |hrsg=Statistics Norway |sprache=no |abruf=" + get_todays_date() + "}}</ref>"  