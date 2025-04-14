import csv
import party
from functools import total_ordering


@total_ordering
class Result:
    def __init__(self, name, percentage, votes, seats, percentage_change):
        self.name = name
        self.percentage = round(float(percentage.replace(",", ".")), 1)
        self.votes = int(votes)
        self.seats = int(seats)
        self.party_obj = party.get_party(name)
        self.percentage_change = round(
            float(percentage_change.replace(",", ".")), 1)

    def __lt__(self, other):
        return self.votes < other.votes

    def __eq__(self, other):
        return self.votes == other.votes

    def print_result(self):
        style = ""
        full_name = self.name
        if self.party_obj != '':
            style = self.party_obj.color + " |"
            full_name = self.party_obj.full_name

        change = 'data-sort-value="' + str(self.percentage_change) + '"|'
        if self.percentage_change < 0:
            change = change + "{{Gefallen}}"
        elif self.percentage_change == 0:
            change = change + "{{Unverändert}}"
        else:
            change = change + "{{Gestiegen}}"

        change = change + (str(abs(self.percentage_change))).replace(".", ",")

        print("|-")
        print('|' + style + ' ||align=left| ' + full_name + ' || ' + str(self.votes) + ' || ' +
              (str(self.percentage)).replace(".", ",") + ' ||' + change + ' || ' + str(
            self.seats) + ' ||data-sort-value=""|')
        # print ("[[" + self.name + "]]: "  " (" + str(self.seats) + ")")


results = []


def __print_table_head(year):
    print('{|class="wikitable sortable" style="text-align:right"')
    print('!colspan=7|Parlamentswahl in Norwegen ' + str(year))
    print("|-")
    print('!rowspan=2 colspan=2|Partei')
    print('!colspan=3|Stimmen')
    print('!colspan=2|Sitze')
    print("|-")
    print("!Zahl")
    print("!in %")
    print("!+/- %")
    print("!Zahl")
    print("!+/- %")


def __print_table_footer():
    print('|- class="hintergrundfarbe5"')
    print(
        "|colspan=\"2\" align=\"left\"|'''Gültige Stimmen''' ||'''-''' || '''100,0''' || ||'''169''' ||{{Unverändert}}")
    print('|- class="hintergrundfarbe5"')
    print("|colspan=\"2\" align=\"left\"|'''Ungültige Stimmen''' || '''-''' || colspan=\"4\"|")
    print('|- class="hintergrundfarbe5"')
    print("|colspan=\"2\" align=\"left\"|'''Abgegebene Stimmen''' ||'''-''' || colspan=\"4\"|")
    print('|- class="hintergrundfarbe5"')
    print(
        "|colspan=\"2\" align=\"left\"|'''Anzahl der Wahlberechtigten und [[Wahlbeteiligung]]''' ||'''-''' || '''-''' "
        "||{{Unverändert}} || colspan=\"2\"|")
    print('|}')


def __print_table(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=";")

        for row in reader:
            party_name = row[7]
            percentage = row[8]
            votes = row[12]
            seats = row[15]
            percentage_change = row[13]

            if party_name != "Partinavn":
                result = Result(party_name, percentage, votes,
                                seats, percentage_change)
                results.append(result)

        results.sort(reverse=True)

        for result in results:
            result.print_result()


def print_election_results(year, path):
    __print_table_head(year)
    __print_table(path)
    __print_table_footer()
