import fylke
import csv

class Municipality():
    def __init__(self, name, number, wikipedia_article = ""):
        self.name = name
        self.number = number
        self.fylke_nr = number[:2]

        if (wikipedia_article == ""):
            self.wikipedia_article = name
        else:
            self.wikipedia_article = name + " (" + wikipedia_article + ")"

    def get_fylke(self):
        return fylke.get_fylke_by_number(self.fylke_nr)

    def get_name(self):
        return self.name
        
    def get_citizen_name(self):
        populationName = ""

        with open('namn.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[1] == self.number:
                    if (populationName == ""):
                        populationName = row[0].capitalize()
                    else:
                        populationName = populationName + "'' oder ''" + row[0].capitalize()
        
        return populationName

    def get_language(self):
        with open('language.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[0] == self.number:
                    return row[2]

        return ""
            
    def get_highest_mountain(self):
        with open('mountains.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row[0] == self.get_fylke().name and row[1] == self.name:
                    return [row[2], row[3]]

        return ""

    def get_wiki_link(self):
        if self.name == self.wikipedia_article:
            return "[[" + self.wikipedia_article + "]]"
        else:
            return "[[" + self.wikipedia_article + "|" + self.name + "]]"
    
    def get_language(self):
        with open('language.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')

            for row in reader:
                if row[0] == self.number:
                    form = row[2]

                    return form
        
        return ""

municipalities = []

def get_municipality_by_name (name):
    if len(municipalities) == 0:
        __create_list()

    for municipality in municipalities:
        if(municipality.name == name):
            return municipality
    
    return ""

def get_municipality_by_number (number):
    if len(municipalities) == 0:
        __create_list()

    for municipality in municipalities:
        if(municipality.number == number):
            return municipality
    
    return ""

def __create_list():
    municipalities.append(Municipality("Alstahaug", "1820"))
    municipalities.append(Municipality("Alta", "5403"))
    municipalities.append(Municipality("Alvdal", "3428"))
    municipalities.append(Municipality("Alver", "4631"))
    municipalities.append(Municipality("Andøy", "1871"))
    municipalities.append(Municipality("Aremark", "3012"))
    municipalities.append(Municipality("Arendal", "4203"))
    municipalities.append(Municipality("Asker", "3025"))
    municipalities.append(Municipality("Askvoll", "4645"))
    municipalities.append(Municipality("Askøy", "4627"))
    municipalities.append(Municipality("Aukra", "1547"))
    municipalities.append(Municipality("Aure", "1576"))
    municipalities.append(Municipality("Aurland", "4641")) 
    municipalities.append(Municipality("Aurskog-Høland", "3026"))
    municipalities.append(Municipality("Austevoll", "4625"))
    municipalities.append(Municipality("Austrheim", "4632"))
    municipalities.append(Municipality("Averøy", "1554"))
    municipalities.append(Municipality("Balsfjord", "5422", "Kommune"))
    municipalities.append(Municipality("Bamble", "3813"))
    municipalities.append(Municipality("Bardu", "5416"))
    municipalities.append(Municipality("Beiarn", "1839"))
    municipalities.append(Municipality("Bergen", "4601", "Norwegen"))
    municipalities.append(Municipality("Berlevåg", "5440"))
    municipalities.append(Municipality("Bindal", "1811"))
    municipalities.append(Municipality("Birkenes", "4216"))
    municipalities.append(Municipality("Bjerkreim", "1114"))
    municipalities.append(Municipality("Bjørnafjorden", "4624"))
    municipalities.append(Municipality("Bodø", "1804"))
    municipalities.append(Municipality("Bokn", "1145"))
    municipalities.append(Municipality("Bremanger", "4648"))
    municipalities.append(Municipality("Brønnøy", "1813"))
    municipalities.append(Municipality("Bygland", "4220"))
    municipalities.append(Municipality("Bykle", "4222"))
    municipalities.append(Municipality("Bærum", "3024"))
    municipalities.append(Municipality("Bø", "1867", "Nordland"))
    municipalities.append(Municipality("Bømlo", "4613"))
    municipalities.append(Municipality("Båtsfjord", "5443"))
    municipalities.append(Municipality("Tana", "5441", "Norwegen"))
    municipalities.append(Municipality("Tjeldsund", "5412", "Kommune"))
    municipalities.append(Municipality("Dovre", "3431"))
    municipalities.append(Municipality("Drammen", "3005"))
    municipalities.append(Municipality("Drangedal", "3815"))
    municipalities.append(Municipality("Dyrøy", "5420"))
    municipalities.append(Municipality("Dønna", "1827"))
    municipalities.append(Municipality("Eidfjord", "4619", "Kommune"))
    municipalities.append(Municipality("Eidskog", "3416"))
    municipalities.append(Municipality("Eidsvoll", "3035"))
    municipalities.append(Municipality("Eigersund", "1101"))
    municipalities.append(Municipality("Elverum", "3420"))
    municipalities.append(Municipality("Enebakk", "3028"))
    municipalities.append(Municipality("Engerdal", "3425"))
    municipalities.append(Municipality("Etne", "4611"))
    municipalities.append(Municipality("Etnedal", "3450"))
    municipalities.append(Municipality("Evenes", "1853", "Kommune"))
    municipalities.append(Municipality("Evje og Hornnes", "4219"))
    municipalities.append(Municipality("Farsund", "4206"))
    municipalities.append(Municipality("Fauske", "1841"))
    municipalities.append(Municipality("Fedje", "4633"))
    municipalities.append(Municipality("Fitjar", "4615"))
    municipalities.append(Municipality("Fjaler", "4646"))
    municipalities.append(Municipality("Fjord", "1578", "Kommune"))
    municipalities.append(Municipality("Flakstad", "1859"))
    municipalities.append(Municipality("Flatanger", "5049"))
    municipalities.append(Municipality("Flekkefjord", "4207"))
    municipalities.append(Municipality("Flesberg", "3050"))
    municipalities.append(Municipality("Flå", "3039"))
    municipalities.append(Municipality("Folldal", "3429"))
    municipalities.append(Municipality("Fredrikstad", "3004"))
    municipalities.append(Municipality("Frogn", "3022"))
    municipalities.append(Municipality("Froland", "4214"))
    municipalities.append(Municipality("Frosta", "5036", "Norwegen"))
    municipalities.append(Municipality("Frøya", "5014"))
    municipalities.append(Municipality("Fyresdal", "3823"))
    municipalities.append(Municipality("Færder", "3811"))
    municipalities.append(Municipality("Kåfjord", "5426", "Kommune"))
    municipalities.append(Municipality("Gamvik", "5439"))
    municipalities.append(Municipality("Gausdal", "3441"))
    municipalities.append(Municipality("Gildeskål", "1838"))
    municipalities.append(Municipality("Giske", "1532"))
    municipalities.append(Municipality("Gjemnes", "1557"))
    municipalities.append(Municipality("Gjerdrum", "3032"))
    municipalities.append(Municipality("Gjerstad", "4211"))
    municipalities.append(Municipality("Gjesdal", "1122"))
    municipalities.append(Municipality("Gjøvik", "3407"))
    municipalities.append(Municipality("Gloppen", "4650"))
    municipalities.append(Municipality("Gol", "3041", "Norwegen"))
    municipalities.append(Municipality("Gran", "3446", "Kommune"))
    municipalities.append(Municipality("Grane", "1825", "Nordland"))
    municipalities.append(Municipality("Gratangen", "5414"))
    municipalities.append(Municipality("Grimstad", "4202"))
    municipalities.append(Municipality("Grong", "5045"))
    municipalities.append(Municipality("Grue", "3417"))
    municipalities.append(Municipality("Gulen", "4635"))
    municipalities.append(Municipality("Kautokeino", "5430"))
    municipalities.append(Municipality("Hamarøy", "1875"))
    municipalities.append(Municipality("Hadsel", "1866"))
    municipalities.append(Municipality("Halden", "3001", "Norwegen"))
    municipalities.append(Municipality("Hamar", "3403"))
    municipalities.append(Municipality("Hammerfest", "5406"))
    municipalities.append(Municipality("Hareid", "1517"))
    municipalities.append(Municipality("Harstad", "5402"))
    municipalities.append(Municipality("Hasvik", "5433"))
    municipalities.append(Municipality("Haugesund", "1106"))
    municipalities.append(Municipality("Heim", "5055", "Norwegen"))
    municipalities.append(Municipality("Hemnes", "1832"))
    municipalities.append(Municipality("Hemsedal", "3042"))
    municipalities.append(Municipality("Herøy", "1818", "Nordland"))
    municipalities.append(Municipality("Herøy", "1515", "Møre og Romsdal"))
    municipalities.append(Municipality("Hitra", "5056"))
    municipalities.append(Municipality("Hjartdal", "3819"))
    municipalities.append(Municipality("Hjelmeland", "1133"))
    municipalities.append(Municipality("Hol", "3044", "Norwegen"))
    municipalities.append(Municipality("Hole", "3038", "Norwegen"))
    municipalities.append(Municipality("Holmestrand", "3802"))
    municipalities.append(Municipality("Holtålen", "5026"))
    municipalities.append(Municipality("Horten", "3801", "Norwegen"))
    municipalities.append(Municipality("Hurdal", "3037"))
    municipalities.append(Municipality("Hustadvika", "1579", "Kommune"))
    municipalities.append(Municipality("Hvaler", "3011"))
    municipalities.append(Municipality("Hyllestad", "4637"))
    municipalities.append(Municipality("Hægebostad", "4226"))
    municipalities.append(Municipality("Høyanger", "4638"))
    municipalities.append(Municipality("Høylandet", "5046"))
    municipalities.append(Municipality("Hå", "1119"))
    municipalities.append(Municipality("Ibestad", "5413"))
    municipalities.append(Municipality("Inderøy", "5053"))
    municipalities.append(Municipality("Indre Fosen", "5054"))
    municipalities.append(Municipality("Indre Østfold", "3014"))
    municipalities.append(Municipality("Iveland", "4218"))
    municipalities.append(Municipality("Jevnaker", "3053"))
    municipalities.append(Municipality("Karasjok", "5437"))
    municipalities.append(Municipality("Karlsøy", "5423"))
    municipalities.append(Municipality("Karmøy", "1149"))
    municipalities.append(Municipality("Kinn", "4602", "Kommune"))
    municipalities.append(Municipality("Klepp", "1120"))
    municipalities.append(Municipality("Kongsberg", "3006"))
    municipalities.append(Municipality("Kongsvinger", "3401"))
    municipalities.append(Municipality("Kragerø", "3814"))
    municipalities.append(Municipality("Kristiansand", "4204"))
    municipalities.append(Municipality("Kristiansund", "1505"))
    municipalities.append(Municipality("Krødsherad", "3046"))
    municipalities.append(Municipality("Kvam", "4622"))
    municipalities.append(Municipality("Kvinesdal", "4227"))
    municipalities.append(Municipality("Kvinnherad", "4617"))
    municipalities.append(Municipality("Kviteseid", "3821"))
    municipalities.append(Municipality("Kvitsøy", "1144"))
    municipalities.append(Municipality("Kvæfjord", "5411", "Kommune"))
    municipalities.append(Municipality("Kvænangen", "5429", "Kommune"))
    municipalities.append(Municipality("Larvik", "3805"))
    municipalities.append(Municipality("Lebesby", "5438"))
    municipalities.append(Municipality("Leirfjord", "1822"))
    municipalities.append(Municipality("Leka", "5052", "Norwegen"))
    municipalities.append(Municipality("Lesja", "3432"))
    municipalities.append(Municipality("Levanger", "5037"))
    municipalities.append(Municipality("Lier", "3049", "Norwegen"))
    municipalities.append(Municipality("Lierne", "5042"))
    municipalities.append(Municipality("Lillehammer", "3405"))
    municipalities.append(Municipality("Lillesand", "4215"))
    municipalities.append(Municipality("Lillestrøm", "3030", "Kommune"))
    municipalities.append(Municipality("Lindesnes", "4205"))
    municipalities.append(Municipality("Lavangen", "5415"))
    municipalities.append(Municipality("Lom", "3434", "Norwegen"))
    municipalities.append(Municipality("Loppa", "5432"))
    municipalities.append(Municipality("Lund", "1112", "Norwegen"))
    municipalities.append(Municipality("Lunner", "3054"))
    municipalities.append(Municipality("Lurøy", "1834"))
    municipalities.append(Municipality("Luster", "4644", "Norwegen"))
    municipalities.append(Municipality("Lyngdal", "4225"))
    municipalities.append(Municipality("Lyngen", "5424"))
    municipalities.append(Municipality("Lærdal", "4642"))
    municipalities.append(Municipality("Lødingen", "1851"))
    municipalities.append(Municipality("Lørenskog", "3029"))
    municipalities.append(Municipality("Løten", "3412"))
    municipalities.append(Municipality("Malvik", "5031"))
    municipalities.append(Municipality("Marker", "3013", "Norwegen"))
    municipalities.append(Municipality("Masfjorden", "4634"))
    municipalities.append(Municipality("Melhus", "5028"))
    municipalities.append(Municipality("Meløy", "1837"))
    municipalities.append(Municipality("Meråker", "5034"))
    municipalities.append(Municipality("Midtre Gauldal", "5027"))
    municipalities.append(Municipality("Midt-Telemark", "3817"))
    municipalities.append(Municipality("Modalen", "4629"))
    municipalities.append(Municipality("Modum", "3047"))
    municipalities.append(Municipality("Molde", "1506"))
    municipalities.append(Municipality("Moskenes", "1874"))
    municipalities.append(Municipality("Moss", "3002"))
    municipalities.append(Municipality("Målselv", "5418"))
    municipalities.append(Municipality("Måsøy", "5434"))
    municipalities.append(Municipality("Namsos", "5007"))
    municipalities.append(Municipality("Namsskogan", "5044"))
    municipalities.append(Municipality("Nannestad", "3036"))
    municipalities.append(Municipality("Narvik", "1806"))
    municipalities.append(Municipality("Nes", "3034", "Akershus"))
    municipalities.append(Municipality("Nesbyen", "3040"))
    municipalities.append(Municipality("Nesna", "1828"))
    municipalities.append(Municipality("Nesodden", "3023"))
    municipalities.append(Municipality("Nissedal", "3822"))
    municipalities.append(Municipality("Nittedal", "3031"))
    municipalities.append(Municipality("Nome", "3816", "Norwegen"))
    municipalities.append(Municipality("Nord-Aurdal", "3451"))
    municipalities.append(Municipality("Nord-Fron", "3436"))
    municipalities.append(Municipality("Nordkapp", "5435"))
    municipalities.append(Municipality("Nord-Odal", "3414"))
    municipalities.append(Municipality("Nordre Follo", "3020"))
    municipalities.append(Municipality("Nordreisa", "5428"))
    municipalities.append(Municipality("Nordre Land", "3448"))
    municipalities.append(Municipality("Nore og Uvdal", "3052"))
    municipalities.append(Municipality("Notodden", "3808"))
    municipalities.append(Municipality("Nærøysund", "5060"))
    municipalities.append(Municipality("Oppdal", "5021"))
    municipalities.append(Municipality("Orkland", "5059"))
    municipalities.append(Municipality("Os", "3430", "Innlandet"))
    municipalities.append(Municipality("Osen", "5020"))
    municipalities.append(Municipality("Oslo", "0301"))
    municipalities.append(Municipality("Osterøy", "4630"))
    municipalities.append(Municipality("Overhalla", "5047"))
    municipalities.append(Municipality("Porsanger", "5436"))
    municipalities.append(Municipality("Porsgrunn", "3806"))
    municipalities.append(Municipality("Rakkestad", "3016"))
    municipalities.append(Municipality("Rana", "1833", "Nordland"))
    municipalities.append(Municipality("Randaberg", "1127"))
    municipalities.append(Municipality("Rauma", "1539", "Kommune"))
    municipalities.append(Municipality("Rendalen", "3424"))
    municipalities.append(Municipality("Rennebu", "5022"))
    municipalities.append(Municipality("Rindal", "5061", "Norwegen"))
    municipalities.append(Municipality("Ringebu", "3439"))
    municipalities.append(Municipality("Ringerike", "3007"))
    municipalities.append(Municipality("Ringsaker", "3411"))
    municipalities.append(Municipality("Risør", "4201"))
    municipalities.append(Municipality("Rollag", "3051"))
    municipalities.append(Municipality("Rælingen", "3027"))
    municipalities.append(Municipality("Rødøy", "1836"))
    municipalities.append(Municipality("Røros", "5025"))
    municipalities.append(Municipality("Røst", "1856"))
    municipalities.append(Municipality("Råde", "3017"))
    municipalities.append(Municipality("Røyrvik", "5043"))
    municipalities.append(Municipality("Salangen", "5417"))
    municipalities.append(Municipality("Saltdal", "1840"))
    municipalities.append(Municipality("Samnanger", "4623"))
    municipalities.append(Municipality("Sande", "1514", "Møre og Romsdal"))
    municipalities.append(Municipality("Sandefjord", "3804"))
    municipalities.append(Municipality("Sandnes", "1108"))
    municipalities.append(Municipality("Sarpsborg", "3003"))
    municipalities.append(Municipality("Sauda", "1135"))
    municipalities.append(Municipality("Sel", "3437"))
    municipalities.append(Municipality("Selbu", "5032"))
    municipalities.append(Municipality("Seljord", "3820"))
    municipalities.append(Municipality("Senja", "5421", "Kommune"))
    municipalities.append(Municipality("Sigdal", "3045"))
    municipalities.append(Municipality("Siljan", "3812", "Norwegen"))
    municipalities.append(Municipality("Sirdal", "4228"))
    municipalities.append(Municipality("Skaun", "5029"))
    municipalities.append(Municipality("Skien", "3807"))
    municipalities.append(Municipality("Skiptvet", "3015"))
    municipalities.append(Municipality("Skjervøy", "5427"))
    municipalities.append(Municipality("Skjåk", "3433"))
    municipalities.append(Municipality("Smøla", "1573"))
    municipalities.append(Municipality("Snåsa", "5041"))
    municipalities.append(Municipality("Sogndal", "4640"))
    municipalities.append(Municipality("Sokndal", "1111"))
    municipalities.append(Municipality("Sola", "1124", "Norwegen"))
    municipalities.append(Municipality("Solund", "4636"))
    municipalities.append(Municipality("Sortland", "1870"))
    municipalities.append(Municipality("Stad", "4649"))
    municipalities.append(Municipality("Stange", "3413", "Norwegen"))
    municipalities.append(Municipality("Stavanger", "1103"))
    municipalities.append(Municipality("Steigen", "1848"))
    municipalities.append(Municipality("Steinkjer", "5006"))
    municipalities.append(Municipality("Stjørdal", "5035"))
    municipalities.append(Municipality("Stord", "4614"))
    municipalities.append(Municipality("Stor-Elvdal", "3423"))
    municipalities.append(Municipality("Storfjord", "5425", "Kommune"))
    municipalities.append(Municipality("Strand", "1130", "Norwegen"))
    municipalities.append(Municipality("Stranda", "1525"))
    municipalities.append(Municipality("Stryn", "4651"))
    municipalities.append(Municipality("Sula", "1531", "Kommune"))
    municipalities.append(Municipality("Suldal", "1134"))
    municipalities.append(Municipality("Sunndal", "1563"))
    municipalities.append(Municipality("Sunnfjord", "4647", "Kommune"))
    municipalities.append(Municipality("Surnadal", "1566"))
    municipalities.append(Municipality("Sveio", "4612"))
    municipalities.append(Municipality("Sykkylven", "1528"))
    municipalities.append(Municipality("Sømna", "1812"))
    municipalities.append(Municipality("Søndre Land", "3447"))
    municipalities.append(Municipality("Sør-Aurdal", "3449"))
    municipalities.append(Municipality("Sørfold", "1845"))
    municipalities.append(Municipality("Sør-Fron", "3438"))
    municipalities.append(Municipality("Sør-Odal", "3415"))
    municipalities.append(Municipality("Sørreisa", "5419"))
    municipalities.append(Municipality("Sør-Varanger", "5444"))
    municipalities.append(Municipality("Time", "1121", "Norwegen"))
    municipalities.append(Municipality("Tingvoll", "1560"))
    municipalities.append(Municipality("Tinn", "3818"))
    municipalities.append(Municipality("Tokke", "3824"))
    municipalities.append(Municipality("Tolga", "3426", "Norwegen"))
    municipalities.append(Municipality("Tromsø", "5401"))
    municipalities.append(Municipality("Trondheim", "5001"))
    municipalities.append(Municipality("Trysil", "3421"))
    municipalities.append(Municipality("Træna", "1835"))
    municipalities.append(Municipality("Tvedestrand", "4213"))
    municipalities.append(Municipality("Tydal", "5033"))
    municipalities.append(Municipality("Tynset", "3427"))
    municipalities.append(Municipality("Tysnes", "4616"))
    municipalities.append(Municipality("Tysvær", "1146"))
    municipalities.append(Municipality("Tønsberg", "3803"))
    municipalities.append(Municipality("Ullensaker", "3033"))
    municipalities.append(Municipality("Ullensvang", "4618"))
    municipalities.append(Municipality("Ulstein", "1516"))
    municipalities.append(Municipality("Ulvik", "4620"))
    municipalities.append(Municipality("Nesseby", "5442"))
    municipalities.append(Municipality("Utsira", "1151"))
    municipalities.append(Municipality("Vadsø", "5405"))
    municipalities.append(Municipality("Vaksdal", "4628", "Kommune"))
    municipalities.append(Municipality("Valle", "4221"))
    municipalities.append(Municipality("Vang", "3454"))
    municipalities.append(Municipality("Vanylven", "1511"))
    municipalities.append(Municipality("Vardø", "5404"))
    municipalities.append(Municipality("Vefsn", "1824"))
    municipalities.append(Municipality("Vega", "1815", "Norwegen"))
    municipalities.append(Municipality("Vegårshei", "4212"))
    municipalities.append(Municipality("Vennesla", "4223"))
    municipalities.append(Municipality("Verdal", "5038"))
    municipalities.append(Municipality("Vestby", "3019"))
    municipalities.append(Municipality("Vestnes", "1535"))
    municipalities.append(Municipality("Vestre Slidre", "3452"))
    municipalities.append(Municipality("Vestre Toten", "3443"))
    municipalities.append(Municipality("Vestvågøy", "1860"))
    municipalities.append(Municipality("Vevelstad", "1816"))
    municipalities.append(Municipality("Vik", "4639", "Kommune"))
    municipalities.append(Municipality("Vindafjord", "1160"))
    municipalities.append(Municipality("Vinje", "3825"))
    municipalities.append(Municipality("Volda", "1577"))
    municipalities.append(Municipality("Voss", "4621", "Norwegen"))
    municipalities.append(Municipality("Værøy", "1857"))
    municipalities.append(Municipality("Vågan", "1865"))
    municipalities.append(Municipality("Vågå", "3435"))
    municipalities.append(Municipality("Våler", "3018", "Viken"))
    municipalities.append(Municipality("Våler", "3419", "Innlandet"))
    municipalities.append(Municipality("Øksnes", "1868"))
    municipalities.append(Municipality("Ørland", "5057"))
    municipalities.append(Municipality("Ørsta", "1520"))
    municipalities.append(Municipality("Østre Toten", "3442"))
    municipalities.append(Municipality("Øvre Eiker", "3048"))
    municipalities.append(Municipality("Øyer", "3440"))
    municipalities.append(Municipality("Øygarden", "4626"))
    municipalities.append(Municipality("Øystre Slidre", "3453"))
    municipalities.append(Municipality("Åfjord", "5058"))
    municipalities.append(Municipality("Ål", "3043"))
    municipalities.append(Municipality("Ålesund", "1507"))
    municipalities.append(Municipality("Åmli", "4217"))
    municipalities.append(Municipality("Åmot", "3422"))
    municipalities.append(Municipality("Hattfjelldal", "1826"))
    municipalities.append(Municipality("Årdal", "4643"))
    municipalities.append(Municipality("Ås", "3021", "Kommune"))
    municipalities.append(Municipality("Åseral", "4224"))
    municipalities.append(Municipality("Åsnes", "3418"))