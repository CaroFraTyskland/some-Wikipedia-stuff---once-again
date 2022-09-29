import kartverketAPI
import municipality
import reference

class MunicipalityArticle:

    def __init__ (self, number, centre):
        self.muni_nr = number
        self.admin_centre = centre

        code = kartverketAPI.get_code_muni_basic(self.muni_nr)
        self.name = kartverketAPI.get_municipality_name(code)
        self.fylke = kartverketAPI.get_fylke(code)
    

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

    def write_geography(self):
        text = "== Geografie ==\n"
        text += self.write_neighbours()
        text += reference.get_source_norgeskart(self.name + " kommune")

        return text

    def write_commuters(self):
        return "Im Jahr 2021 arbeiteten von rund x Arbeitstätigen etwa x in " + self.name + " selbst, ." + reference.get_source_ssb_commuter()

    def write_infrastructor_economy(self):
        return "== Wirtschaft und Infrastruktur ==\n=== Verkehr ===\n<ref name=\"norgeskart\" />\n\n=== Wirtschaft ===\n" + reference.get_soure_snl(self.name) + " " + self.write_commuters()

def write_article(muni_nr, admin_centre):
    article = MunicipalityArticle(muni_nr, admin_centre)

    return article.write_geography() + "\n\n" + article.write_infrastructor_economy()