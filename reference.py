from datetime import datetime

def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d')

def build_reference(source):
    return "<ref>" + source + "</ref>"

def build_reference_with_name(name, source):
    return "<ref name=\"" + name + "\">" + source + "</ref>"

def get_source_norgeskart(place_name):
    return build_reference_with_name("norgeskart", "{{Internetquelle |url= |titel=" + place_name + " |abruf= " + get_todays_date() + " |werk=Norgeskart |sprache=no}}")

def get_snl_url(name):
    name = name.replace(" ", "_")
    return "https://snl.no/" + name

def get_soure_snl(name):
    return "<ref name=\"snl\">{{Internetquelle |autor= |url=" + get_snl_url(name) + " |titel=" + name + " |abruf=" + get_todays_date() + " |werk=Store norske leksikon |sprache=no}}</ref>"

def get_source_ssb_commuter():
     return "<ref>{{Internetquelle |url=https://statisticsnorway.shinyapps.io/pendling/ |titel=Pendlingsstrømmer |hrsg=Statistics Norway |abruf=" + get_todays_date() + " |sprache=no}}</ref>"  