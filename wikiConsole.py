import articlesFromCategory
import copyVioCheck

def print_help():
    help = "cat:\tprint articles from category\n"
    help = help + "cv:\tchecks articles for possible copyright violations (via copyvios.toolforge.org) -> can take forever\n"
    help = help + "help:\toverview over commands"

    print (help)

while (True):
    command = input(">> ")
    command = command.lower()

    if command == "cat":
        cat = input("Name der Kategorie: ")
        articlesFromCategory.print_articles_cat(cat)

    elif command == "copyvios" or command == "cv":
        article = input("zu prüfender Artikel: ")
        copyVioCheck.get_possible_violation(article)

    elif command == "help" or command == "h":
        print_help()