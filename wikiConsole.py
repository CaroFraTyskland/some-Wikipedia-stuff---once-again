import categoryMembers
import categoriesFromArticle
import copyVioCheck
import valgresultat
import editCount

def print_help():
    help = "ac:\tprints categories from an article\n"
    help = help + "cat:\tprints articles from a category and its subcategories\n"
    help = help + "cv:\tchecks articles for possible copyright violations (via copyvios.toolforge.org) -> can take forever\n"
    help = help + "ec:\tprints the edit count of a user\n"
    help = help + "help:\toverview over commands\n"
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

    elif command == "subcats" or command == "sc":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_subcats_cat(cat)

    elif command == "valg":
        year = input("Jahr: ")
        path = input("Pfad zur CSV-Datei: ")

        valgresultat.print_election_results(year, path)