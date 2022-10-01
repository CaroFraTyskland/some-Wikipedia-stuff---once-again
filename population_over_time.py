import csv
import reference
import requests
from contextlib import closing

def __get_list(muni_nr):
    url = "https://data.ssb.no/api/v0/dataset/26975.csv?lang=en"

    lines = []

    with closing(requests.get(url, stream=True)) as r:
        f = (line.decode('latin-1') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')

        for row in reader:
            if str(muni_nr) in row[0]:
                year = int(row[1])

                if year == 1986 or year % 5 == 0:
                    lines.append(row)

    return lines

def get_population_table(muni_nr):
    lines = __get_list(muni_nr)

    table = "{| class=\"wikitable\"\n! Jahr"

    #add years
    for line in lines:
        table = table + " !! " + line[1]
    
    table = table + "\n|-\n| '''Einwohnerzahl'''" + reference.get_source_ssb_pop_over_time()

    #add number of inhabitants (format: 10000 -> 10,000 -> 10.000)
    for line in lines:
        population = "{:,}".format(int(line[3]))
        table = table + " || " + population.replace(",", ".")

    return table + "\n|}"