import categoryMembers
import categoriesFromArticle
import copyVioCheck
import valgresultat
import editCount
import fylke
import municipality
import kartverketAPI
import municipalityArticle

def print_help():
    help = "ac:\tprints categories from an article\n"
    help = help + "cat:\tprints articles from a category and its subcategories\n"
    help = help + "cv:\tchecks articles for possible copyright violations (via copyvios.toolforge.org) -> can take forever\n"
    help = help + "ec:\tprints the edit count of a user\n"
    help = help + "help:\toverview over commands\n"
    help = help + "m:\tprints the Wikipedia article for a municipality\n"
    help = help + "m -name:\tprints name of municipality with a certain municipality number\n"
    help = help + "sc:\tprints subcategories from a category and its subcategories"
    help = help + "valg:\tprints the table with the election results; needs path to csv file (https://valgresultat.no/?type=st -> Eksport av valgresultater -> Partifordeling (Landsnivå)"

    print (help)

while (True):
    command = input(">> ")
    command = command.lower()

    if command == "ac":
        article = input("Name des Artikels: ")
        categoriesFromArticle.print_cats_from_article(article)

    if command == "cat":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_articles_cat(cat)

    elif command == "copyvios" or command == "cv":
        article = input("zu prüfender Artikel: ")
        copyVioCheck.get_possible_violation(article)

    if command == "ec":
        user = input("Username: ")
        editCount.print_edit_count(user)

    elif command == "help" or command == "h":
        print_help()

    if command == "m" or command == "muni":
        number = input("Kommunennummer: ")
        admin_centre = input("Verwaltungszentrum: ")
        print(municipalityArticle.write_article(number, admin_centre))

    elif command == "m -name" or command == "muni -name":
        number = input("Kommunennummer: ")
        try:
            print (municipality.get_municipality_by_number(number).name)
        except:
            print ("keine gültige Nummer")

    elif command == "m -nr" or command == "muni -nr":
        name = input("Name der Kommune: ")
        try:
            print (municipality.get_municipality_by_name(name).number)
        except:
            print ("keine gültiger Name")

    elif command == "subcats" or command == "sc":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_subcats_cat(cat)

    elif command == "valg":
        year = input("Jahr: ")
        path = input("Pfad zur CSV-Datei: ")

        valgresultat.print_election_results(year, path)