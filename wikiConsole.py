import categoryMembers
import copyVioCheck

def print_help():
    help = "cat:\tprints articles from a category and its subcategories\n"
    help = help + "cv:\tchecks articles for possible copyright violations (via copyvios.toolforge.org) -> can take forever\n"
    help = help + "help:\toverview over commands\n"
    help = help + "sc:\tprints subcategories from a category and its subcategories"

    print (help)

while (True):
    command = input(">> ")
    command = command.lower()

    if command == "cat":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_articles_cat(cat)

    elif command == "copyvios" or command == "cv":
        article = input("zu prüfender Artikel: ")
        copyVioCheck.get_possible_violation(article)

    elif command == "help" or command == "h":
        print_help()

    elif command == "subcats" or command == "sc":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_subcats_cat(cat)