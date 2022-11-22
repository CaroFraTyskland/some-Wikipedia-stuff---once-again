class Fylke():
    def __init__(self, name, wikipedia_article, still_exits, number):
        self.name = name
        self.number = number
        self.still_exists = still_exits
        self.wikipedia_article = wikipedia_article

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
    
    def get_wiki_link(self):
        if self.name == self.wikipedia_article:
            return "[[" + self.name + "]]"
        else:
            return "[[" + self.wikipedia_article + "|" + self.name + "]]"

fylker = []

def get_fylke_by_number (number):
    if len(fylker) == 0:
        __create_list()

    for fylke in fylker:
        if str(fylke.number) == str(number):
            return fylke
    
    return ""

def get_fylke_by_name (name):
    if len(fylker) == 0:
        __create_list()
        
    for fylke in fylker:
        if(fylke.name.lower() == name.lower()):
            return fylke
    
    return ""

def is_new (fylke_nr):
    return fylke_nr in ("42", "34", "54", "50", "38", "46", "30")


def __create_list():
    fylker.append(Fylke("Agder", "Agder", True, "42"))
    fylker.append(Fylke("Innlandet", "Innlandet", True, "34"))
    fylker.append(Fylke("Møre og Romsdal", "Møre og Romsdal", True, "15"))
    fylker.append(Fylke("Nordland", "Nordland", True, "18"))
    fylker.append(Fylke("Oslo", "Oslo", True, "03"))
    fylker.append(Fylke("Rogaland", "Rogaland", True, "11"))
    fylker.append(Fylke("Troms og Finnmark", "Troms og Finnmark", True, "54"))
    fylker.append(Fylke("Trøndelag", "Trøndelag", True, "50"))
    fylker.append(Fylke("Vestfold og Telemark", "Vestfold og Telemark", True, "38"))
    fylker.append(Fylke("Vestland", "Vestland", True, "46"))
    fylker.append(Fylke("Viken", "Viken", True, "30"))

    fylker.append(Fylke("Akershus", "Akershus", False, "02"))
    fylker.append(Fylke("Aust-Agder", "Aust-Agder", False, "09"))
    fylker.append(Fylke("Buskerud", "Buskerud", False, "06"))
    fylker.append(Fylke("Finnmark", "Finnmark (Fylke)", False, "20"))
    fylker.append(Fylke("Hedmark", "Hedmark", False, "04"))
    fylker.append(Fylke("Hordaland", "Hordaland", False, "12"))
    fylker.append(Fylke("Nord-Trøndelag", "Nord-Trøndelag", False, "17"))
    fylker.append(Fylke("Østfold", "Østfold", False, "01"))
    fylker.append(Fylke("Oppland", "Oppland", False, "05"))
    fylker.append(Fylke("Sør-Trøndelag", "Sør-Trøndelag", False, "16"))
    fylker.append(Fylke("Sogn og Fjordane", "Sogn og Fjordane", False, "14"))
    fylker.append(Fylke("Telemark", "Telemark", False, "08"))
    fylker.append(Fylke("Troms", "Troms", False, "19"))
    fylker.append(Fylke("Vest-Agder", "Vest-Agder", False, "10"))
    fylker.append(Fylke("Vestfold", "Vestfold", False, "07"))