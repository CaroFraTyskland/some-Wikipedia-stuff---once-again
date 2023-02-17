import tettsted
import municipality
import reference
import category
import kartverketAPI
import famousPeople


class TettstedArticle:

    def __init__(self, number, is_city, is_muni_center):
        self.number = number
        self.is_city = is_city
        self.is_muni_center = is_muni_center

        list = tettsted.get_tettsted_by_tettsted_nr(number)

        if len(list) == 1:
            row = list[0]
            self.name = row[1]
            self.muni_nr = row[2]
            self.pop = row[3]
            self.area = row[4]

        self.muni = municipality.get_municipality_by_number(self.muni_nr)
        self.fylke = self.muni.get_fylke()

        self.code = kartverketAPI.get_code_stedsnavn_tettsted(self.name, self.muni_nr)

        self.lat = kartverketAPI.get_coord_lat(self.code)
        self.long = kartverketAPI.get_coord_long(self.code)

    def write_infobox(self):
        text = "\n{{Infobox Ort in Norwegen\n" \
               "| Fylke = " + self.fylke.get_number() + "\n" \
               "| Kommune = " + self.muni.get_wiki_link() + "\n" \
               "| lat_deg = " + self.lat + "\n" \
               "| lon_deg = " + self.long + "\n" \
               "| Einwohner = {{Metadaten Einwohnerzahl Ort NO|" + self.number + "}}\n" \
               "| Stand = {{EWD|Ort NO|}}\n" \
               "| Fläche = {{Metadaten Fläche Ort NO|" + self.number + "}}\n" \
               "| Höhe = \n" \
               "| Straßen = \n" \
               "| Schienen = \n" \
               "| Flughafen = \n" \
               "| Bild = \n" \
               "| Bildunterschrift = \n" \
               "}}"

        return text

    def write_first_paragraph(self):
        text = "'''" + self.name + "'''" + " ist eine "

        if self.is_city:
            text += "Stadt"
        else:
            text += "Ortschaft"

        text += " in der [[Norwegen|norwegischen]] Kommune " + self.muni.get_wiki_link() + " in der Provinz ([[Fylke]]) [[" + self.fylke.get_name() + "]]. "

        if self.is_city:
            text += "Die Stadt "
        else:
            text += "Der Ort "

        if self.is_muni_center:
            text += "stellt das Verwaltungszentrum von " + self.muni.get_name() + " dar und "

        text += "hat {{EWZ|Ort NO|" + self.number + "}} Einwohner (Stand: {{EWD|Ort NO|}}).<ref name=\"ssb\">{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

        return text

    def write_basic_structure(self):
        text = "== Geografie ==\n" + self.name
        text += " ist ein sogenannter [[Tettsted]], also eine Ansiedlung, die für statistische Zwecke als eine " \
                "Ortschaft gewertet wird.<ref name=\"ssb\" />\n\n "
        text += reference.get_source_norgeskart(self.name)
        text += "\n\n== Geschichte ==" \
                "\n\n== Wirtschaft und Infrastruktur ==" \
                "\n\n== Name ==\n"
        text += self.name + " wurde im Jahr ... als ''...'' erwähnt. Der Name setzt sich aus den beiden Bestandteilen „...“ und „...“ zusammen, erster leitet sich von ... ab, „...“ steht hingegen für „...“." + reference.get_source_stadnamn(
            self.name)

        return text

    def write_famous_people(self):
        return "== Persönlichkeiten ==" + famousPeople.get_list(self.name)

    def write_weblinks(self):
        return "== Weblinks ==\n{{Commonscat}}\n" + reference.get_snl_weblink(
            self.name) + "\n\n== Einzelnachweise ==\n<references />"

    def write_ending(self):
        text = ""

        if (category.needs_default_sort(self.name)):
            text += category.get_default_sort(self.name)
            text += "\n"

        text += "[[Kategorie:" + self.muni.wikipedia_article + "]]\n"

        return text

    def write_article(self):
        return self.write_infobox() + "\n\n" + self.write_first_paragraph() + "\n\n" + self.write_basic_structure() + "\n\n" + self.write_famous_people() + "\n\n" + self.write_weblinks() + "\n\n" + self.write_ending()


def write_article(tett_number, is_city, is_muni_center):
    article = TettstedArticle(tett_number, is_city, is_muni_center)
    return article.write_article()
