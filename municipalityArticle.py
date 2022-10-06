import kartverketAPI
import municipality
import reference
import famousPeople
import population_over_time
import muniArea
import fylke
import tettsted
class MunicipalityArticle:

    def __init__ (self, number, centre):
        self.muni_nr = number
        self.admin_centre = centre

        self.muni = municipality.get_municipality_by_number(self.muni_nr)
        self.fylke = self.muni.get_fylke()

        self.code = kartverketAPI.get_code_muni_basic(self.muni_nr)
        self.name = kartverketAPI.get_municipality_name(self.code)

    def write_first_paragraph(self):
        text = "'''" + self.name + "'''" + " ist eine [[Kommune (Norwegen)|]] im [[Norwegen|norwegischen]] [[Fylke]] " + self.fylke.get_wiki_link() + ". Die Kommune hat {{EWZ|NO|" + self.muni_nr + "}} Einwohner (Stand: {{EWD|NO|" + self.muni_nr + "}}). Verwaltungssitz ist "

        if (self.admin_centre == self.name):
            return text + "der gleichnamige Ort " + self.admin_centre + "."
        else:
            return text + "die Ortschaft [[" + self.admin_centre + "]]."

    def write_neighbours(self):
        neighbours = kartverketAPI.get_neighbour_munis(self.muni_nr)

        text = "Die Gemeinde grenzt an "

        for i in range(len(neighbours)):
            if i == 0:
                text += municipality.get_municipality_by_number(neighbours[i]).get_wiki_link()
            elif i < len(neighbours) - 1:
                text = text + ", " + municipality.get_municipality_by_number(neighbours[i]).get_wiki_link()
            else:
                text = text + " und " + municipality.get_municipality_by_number(neighbours[i]).get_wiki_link()

        return text + "."
    
    def write_highest_mountain(self):
        mountain = self.muni.get_highest_mountain()

        mountain_name = mountain[0]
        height = mountain[1].replace(",", ".")

        if "," in mountain_name:
            mountain_name = mountain_name.replace(",", " (samisch '''") + "''')"

        return "Die Erhebung " + mountain_name + " stellt mit einer Höhe von {{Höhe|" + height + "|NO}} den höchsten Punkt der Kommune " + self.name + " dar." + reference.get_source_highest_mountain(); 
        
    
    def write_famous_people(self):
        return "== Persönlichkeiten ==" + famousPeople.get_list(self.name)

    def write_geography(self):
        text = "== Geografie ==\n" +  self.write_neighbours() + reference.get_source_norgeskart(self.name + " kommune")

        waterArea = str(muniArea.get_water_area(self.muni_nr)).replace(".", ",")

        text += " Die Gesamtfläche der Kommune beträgt {{FL|NO|" + self.muni_nr + "|2}}&nbsp;km², wobei [[Binnengewässer]] zusammen " + waterArea + "&nbsp;km² ausmachen."
        text += reference.get_source_ssb_area_type()

        text = text + "\n\n" + self.write_highest_mountain()

        return text

    def write_new_fylke(self):
        text = "Bis zum "

        fylke_name = self.fylke.name

        if fylke_name == "Trøndelag":
            text += "31. Dezember 2017 gehörte " + self.name + " dem damaligen Fylke [[-Trøndelag]] an. Dieses ging im Zuge der [[Regionalreform in Norwegen]] in das zum 1. Januar 2018 neu geschaffene Fylke " + fylke_name + " über."
        else:
            text += "31. Dezember 2019 gehörte " + self.name + " dem damaligen Fylke [[]] an. Dieses ging im Zuge der [[Regionalreform in Norwegen]] in das zum 1. Januar 2020 neu geschaffene Fylke " + fylke_name + " über."

        return text + reference.get_source_reg_reform_2020()

    def write_history(self):
        text = "== Geschichte ==\n" + reference.get_source_ssb_muni_history()

        if fylke.is_new(self.fylke.number):
            text += " " + self.write_new_fylke()

        return text

    def write_tettsteder(self):
        list = tettsted.get_tettsted_list_muni(self.muni_nr)

        if (len(list) == 0):
            return "In der gesamten Gemeinde liegen keine [[Tettsted]]er, also keine Ansiedlungen, die für statistische Zwecke als eine Ortschaft gewertet werden.<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"
        

        if (len(list) == 1):
            row = list[0]

            text = row[0] + " ist der einzige sogenannte [[Tettsted]], also die einzige Ansiedlung, die für statistische Zwecke als eine Ortschaft gewertet wird."
            if (row[1] == row[2]):
                text+= "Zum {{EWD|Ort NO|}} lebten dort {{EWZ|Ort NO|" + row[1] + "}} Einwohner.<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"
            else:
                text+= "Zum {{EWD|Ort NO|}} lebten in der Kommune " + self.name + " {{EWZ|Ort NO|" + row[1] + "}} der insgesamt {{EWZ|Ort NO|" + row[2] + "}} Einwohner des Tettsteds.<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"
             
            return text   

        if (len(list) == 2):
            r1 = list[0]
            r2 = list[1]

            text = "In der Gemeinde liegen zwei sogenannte [[Tettsted]]er, also zwei Ansiedlungen, die für statistische Zwecke als eine Ortschaft gewertet werden. Diese sind "

            if (r1[1] == r1[2]):
                text += r1[0] + " mit {{EWZ|Ort NO|" + r1[1] + "}} und "
            else:
                text += r1[0] + " mit {{EWZ|Ort NO|" + r1[1] + "}} der insgesamt {{EWZ|Ort NO|" + r1[2] + "}} Einwohner des Tettsteds und "
                
            if (r2[1] == r2[2]):
                text += r2[0] + " mit {{EWZ|Ort NO|" + r2[1] + "}} Einwohnern"
            else:
                text += r2[0] + " mit {{EWZ|Ort NO|" + r2[1] + "}} der insgesamt {{EWZ|Ort NO|" + r2[2] + "}} Einwohner des Tettsteds"
                
            return text + " (Stand: {{EWD|Ort NO|}}).<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"    

        text = "In der Gemeinde liegen mehrere sogenannte [[Tettsted]]er, also mehrere Ansiedlungen, die für statistische Zwecke als eine Ortschaft gewertet werden. Diese sind "

        for i in range(len(list)):
            row = list[i]
            
            if (i < len(list) - 1):
                if (row[1] == row[2]):
                    text += row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}}, "
                else:
                    text += row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}} der insgesamt {{EWZ|Ort NO|" + row[2] + "}} Einwohner des Tettsteds, "
            else:
                if (row[1] == row[2]):
                    text += " und " + row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}} Einwohnern (Stand: {{EWD|Ort NO|}}).<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"
                else:
                    text += " und " + row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}} der insgesamt {{EWZ|Ort NO|" + row[2] + "}} Einwohner des Tettsteds (Stand: {{EWD|Ort NO|}}).<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

        return text
    
    def write_citizen_name(self):
        citizenName = self.muni.get_citizen_name()

        if (citizenName == ""):
            return ""

        citizenName = citizenName.replace(", ", "'' oder ''")

        return "Die Einwohner der Gemeinde werden ''" + citizenName + "'' genannt." + reference.get_source_sprakradet()

    def write_language(self):
        language = self.muni.get_language()

        fylke_name = self.fylke.name
        fylke_nr = self.muni.fylke_nr

        if (language == "bokmål"):
            if fylke_nr in ("34", "30", "18", "54"): #Innlandet, Viken, Nordland, ToF
                text = "Offizielle Schriftsprache ist wie in vielen Kommunen in " + fylke_name + " [[Bokmål]], also die weiter verbreitete der beiden norwegischen Sprachformen."
            elif fylke_nr in ("38", "11"): #VoT, Rogaland
                text = "Offizielle Schriftsprache ist wie in nur wenigen Kommunen in " + fylke_name + " [[Bokmål]], also die weiter verbreitete der beiden norwegischen Sprachformen."
            elif fylke_nr in ("42", "50"):
                text = "Offizielle Schriftsprache ist wie in einigen weiteren Kommunen in " + fylke_name + " [[Bokmål]], also die weiter verbreitete der beiden norwegischen Sprachformen."

        elif (language == "nynorsk"):
            if fylke_nr in ("34", "30"): #Innlandet, Viken
                text = "Offizielle Schriftsprache ist wie in nur wenigen Kommunen in " + fylke_name + " [[Nynorsk]], also die weniger weit verbreitete der beiden norwegischen Sprachformen."
            elif fylke_nr in ("11", "46", "15"): #Rogaland, Vestland, Møre
                text = "Offizielle Schriftsprache ist wie in vielen Kommunen in " + fylke_name + " [[Nynorsk]], also die weniger weit verbreitete der beiden norwegischen Sprachformen."
            elif fylke_nr in ("42", "38"): #Agder, VoT
                text = "Offizielle Schriftsprache ist wie in einigen weiteren Kommunen in " + fylke_name + " [[Nynorsk]], also die weniger weit verbreitete der beiden norwegischen Sprachformen."

        elif (language == "nøytral"):
            if fylke_nr in ("34", "18", "54", "38", "42", "11", "50"): #Innlandet, Nordland, ToF, VoT, Agder, Rogaland, Trøndelag
                text = self.name + " hat wie viele andere Kommunen der Provinz " + fylke_name + " weder [[Nynorsk]] noch [[Bokmål]] als offizielle Sprachform, sondern ist in dieser Frage neutral."
            elif fylke_nr in ("30", "15"): #Viken, Møre
                text = self.name + " hat wie einige weitere Kommunen der Provinz " + fylke_name + " weder [[Nynorsk]] noch [[Bokmål]] als offizielle Sprachform, sondern ist in dieser Frage neutral."
            elif fylke_nr == "46": #Vestland
                text = "Im Gegensatz zu den meisten anderen Kommunen der Provinz " + fylke_name + " hat " + self.name + " weder [[Nynorsk]] noch [[Bokmål]] als offizielle Sprachform, sondern ist in dieser Frage neutral."
            elif fylke_nr == "03":
                text = self.name + " hat weder [[Nynorsk]] noch [[Bokmål]] als offizielle Sprachform, sondern ist in dieser Frage neutral."

        text += reference.get_source_language()

        if kartverketAPI.is_samisk_forvaltningsomrade(self.code):
            text += " Da " + self.name + " Teil des samischen Verwaltungsgebiets ist, ist die norwegische Sprache dem [[Samische Sprachen|Samischen]] gleichgestellt. Die Einwohner haben dadurch unter anderem einen Anspruch darauf, die Kommunikation mit öffentlichen Organen in einer samischen Sprache laufen zu lassen." + reference.get_source_reg_sami()

        return text

    def write_population(self):
        text = "== Einwohner ==\n<ref name=\"snl\" /> " + self.write_tettsteder() + "\n\n"

        citizenNameText = self.write_citizen_name()
        
        if (citizenNameText != ""):
            text += citizenNameText + " "

        text += self.write_language()
        text += "\n\n"

        text += population_over_time.get_population_table(self.muni_nr)

        return text

    def write_commuters(self):
        return "Im Jahr 2021 arbeiteten von rund x Arbeitstätigen etwa x in " + self.name + " selbst, ." + reference.get_source_ssb_commuter()

    def write_infrastructor_economy(self):
        return "== Wirtschaft und Infrastruktur ==\n=== Verkehr ===\n<ref name=\"norgeskart\" />\n\n=== Wirtschaft ===\n" + reference.get_soure_snl(self.name) + " " + self.write_commuters()

    def write_name(self):
        return self.name + " wurde im Jahr ... als ''...'' erwähnt. Der Name setzt sich aus den beiden Bestandteilen „...“ und „...“ zusammen, erster leitet sich von ... ab, „...“ steht hingegen für „...“." +  reference.get_source_stadnamn(self.name)

    def write_name_coat_of_arms(self):
        return "== Name und Wappen ==\nDas seit x offizielle Wappen der Kommune zeigt ... " + self.write_name()

    def write_weblinks(self):
        return "== Weblinks ==\n{{Commonscat}}\n" + reference.get_snl_weblink(self.name) + "\n" + reference.get_ssb_muni_weblink(self.name)

    def write_article(self):
        return self.write_first_paragraph() + "\n\n" + self.write_geography() + "\n\n" + self.write_population() + "\n\n" + self.write_history() + "\n\n" + self.write_infrastructor_economy() + "\n\n" + self.write_name_coat_of_arms() + "\n\n" + self.write_famous_people() + "\n\n" + self.write_weblinks() + "\n\n"

def write_article(muni_nr, admin_centre):
    article = MunicipalityArticle(muni_nr, admin_centre)
    return article.write_article()    