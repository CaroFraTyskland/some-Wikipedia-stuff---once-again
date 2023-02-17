import categoryMembers
import categoriesFromArticle
import copyVioCheck
import valgresultat
import editCount
import fylke
import tettsted
import municipality
import municipalityArticle
import population_over_time
import checkForDeadLinks
import tettstedArticle
import famousPeople


def print_help():
    help = "ac:\tprints categories from an article\n" \
           "cat:\tprints articles from a category and its subcategories\n" \
           "cv:\tchecks articles for possible copyright violations (via copyvios.toolforge.org) -> can take " \
           "forever\n" \
           "dl -a:\tchecks article for dead links\n" \
           "dl -cat:\tchecks category for dead links\n" \
           "ec:\tprints the edit count of a user\n" \
           "f -name:\tprints name of fylke with a certain fylke number\n" \
           "f -nr:\tprints a fylke number of a fylke with a certain name\n" \
           "help:\toverview over commands\n" \
           "m:\tprints the Wikipedia article for a municipality\n" \
           "m -name:\tprints name of municipality with a certain municipality number\n" \
           "m -nr:\tprints a municipality number of a municipality with a certain name\n" \
           "pers -t:\tprints a list of people from a given place\n" \
           "pop -t:\tprints the table with the population development of a municipality\n" \
           "q:\tquit\n" \
           "sc:\tprints subcategories from a category and its subcategories\n" \
           "tett:\tprints the Wikipedia article for a tettsted\n" \
           "valg:\tprints the table with the election results; needs path to csv file (" \
           "https://valgresultat.no/?type=st -> Eksport av valgresultater -> Partifordeling (Landsnivå) "

    print(help)


# asks user for a municipality number until he enters a valid one
def get_muni_number():
    accepted = False
    while not accepted:
        muni_number = input("Kommunennummer: ")

        if municipality.get_municipality_by_number(muni_number) != "":
            accepted = True
        else:
            print("keine gültige Nummer")

    return muni_number


# asks user for a fylke number until he enters a valid one
def get_fylke_number():
    accepted = False
    while not accepted:
        fylke_number = input("Fylkesnummer: ")

        if fylke.get_fylke_by_number(fylke_number) != "":
            accepted = True
        else:
            print("keine gültige Nummer")

    return fylke_number


# asks user a yes/no question until he enters a valid one
def get_input_yn(question):
    while True:
        answer = input(question + " (y/n): ")

        if answer == "y" or answer == "yes" or answer == "j" or answer == "ja":
            return True
        elif answer == "n" or answer == "no" or answer == "nein":
            return False


quit = False
while not quit:
    command = input(">> ")
    command = command.lower()

    if command == "ac":
        article = input("Name des Artikels: ")
        categoriesFromArticle.print_cats_from_article(article)

    elif command == "cat":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_articles_cat(cat)

    elif command == "copyvios" or command == "cv":
        article = input("zu prüfender Artikel: ")
        copyVioCheck.get_possible_violation(article)

    elif command == "dl -a":
        article = input("Artikel: ")
        checkForDeadLinks.test_article(article)

    elif command == "dl -cat":
        cat = input("Kategorie: ")
        checkForDeadLinks.check_category(cat)

    elif command == "ec":
        user = input("Username: ")
        editCount.print_edit_count(user)

    elif command == "f -name" or command == "fylke -name":
        number = get_fylke_number()
        print(fylke.get_fylke_by_number(number).name)

    elif command == "f -nr" or command == "fylke -nr":
        name = input("Name des Fylkes: ")
        try:
            print(fylke.get_fylke_by_name(name).number)
        except:
            print("keine gültiger Name")

    elif command == "help" or command == "h":
        print_help()

    elif command == "m" or command == "muni":
        number = get_muni_number()
        admin_centre = input("Verwaltungszentrum: ")
        print("\n")
        print(municipalityArticle.write_article(number, admin_centre))

    elif command == "m -name" or command == "muni -name":
        number = get_muni_number()
        print(municipality.get_municipality_by_number(number).name)

    elif command == "m -nr" or command == "muni -nr":
        name = input("Name der Kommune: ")
        try:
            print(municipality.get_municipality_by_name(name).number)
        except:
            print("keine gültiger Name")

    elif command == "pers":
        place = input("Ort: ")
        print(famousPeople.get_list(place))

    elif command == "pop -t":
        number = get_muni_number()
        print(population_over_time.get_population_table(number))

    elif command == "q" or command == "quit":
        print("## quit ##")
        quit = True

    elif command == "subcats" or command == "sc":
        cat = input("Name der Kategorie: ")
        categoryMembers.print_subcats_cat(cat)

    elif command == "tett" or command == "tettsted":
        number = input("Tettstednummer: ")
        is_city = get_input_yn("Stadt")
        is_admin_centre = get_input_yn("Verwaltungszentrum")
        print("\n")
        print(tettstedArticle.write_article(number, is_city, is_admin_centre))

    elif command == "tett -meta" or command == "tettsted -meta":
        print("\n")
        print(tettsted.print_metadata_tettsted())

    elif command == "tett -meta -a" or command == "tettsted -meta -area":
        print("\n")
        print(tettsted.print_metadata_tettsted_area())

    elif command == "tett -muni":
        number = get_muni_number()
        print("\n")
        print(tettsted.write_tettsteder_muni(number, municipality.get_municipality_by_number(number).get_name()))

    elif command == "valg":
        year = input("Jahr: ")
        path = input("Pfad zur CSV-Datei: ")

        valgresultat.print_election_results(year, path)