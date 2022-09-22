from enum import Enum

class Party():
    def __init__(self, name, abbreviation, abbreviation_list, member_cat, description, link):
        self.name = name
        self.abbreviation = abbreviation
        self.abbreviation_list = abbreviation_list
        self.member_cat = member_cat
        self.description = description
        self.link = link

        self.full_name = link + " (" + abbreviation + ")"

        self.color = 'style="background:#{{Wahldiagramm/Partei|' + abbreviation + '|dunkel|NO}};"'
            

    def print_info (self):
        print (self.name + " (" + self.abbreviation + ") ")


parties = []
parties.append(Party("Høyre", "H", "Høyre", "Høyre-Mitglied", "konservativen Partei [[Høyre]]", "[[Høyre]]"))
parties.append(Party("Arbeiderpartiet", "Ap", "Ap", "Arbeiderpartiet-Mitglied", "sozialdemokratischen [[Arbeiderpartiet]] (Ap)", "[[Arbeiderpartiet]]"))
parties.append(Party("Kristelig Folkeparti", "KrF", "KrF", "Kristelig-Folkeparti-Mitglied", "christdemokratischen [[Kristelig Folkeparti]] (KrF)", "[[Kristelig Folkeparti]]"))
parties.append(Party("Venstre", "V", "Venstre", "Venstre-Mitglied (Norwegen)", "sozialliberalen [[Venstre (Norwegen)|]]", "[[Venstre (Norwegen)|Venstre]]"))
parties.append(Party("Fremskrittspartiet", "FrP", "FrP", "Fremskrittspartiet-Mitglied", "rechten [[Fremskrittspartiet]] (FrP)", "[[Fremskrittspartiet]]"))
parties.append(Party("Sosialistisk Venstreparti", "SV", "SV", "Sosialistisk-Venstreparti-Mitglied", "[[Sosialistisk Venstreparti]] (SV)", "[[Sosialistisk Venstreparti]]"))
parties.append(Party("Miljøpartiet De Grønne", "MDG", "MDG", "Miljøpartiet-De-Grønne-Mitglied", "grünen [[Miljøpartiet De Grønne]] (MDG)", "[[Miljøpartiet De Grønne]]"))
parties.append(Party("Senterpartiet", "Sp", "Sp", "Senterpartiet-Mitglied", "[[Senterpartiet]] (Sp)", "[[Senterpartiet]]"))
parties.append(Party("Rødt", "R", "Rødt", "Rødt-Mitglied", "linken Partei [[Rødt]]", "[[Rødt]]"))
parties.append(Party("Pasienfokus", "PF", "Pasientfokus", "", "Partei [[Pasientfokus]] (PF)", "[[Pasientfokus]]"))


def get_party (name):
    for party in parties:
        if(party.name == name):
            return party
    
    return ""