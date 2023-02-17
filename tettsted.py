import csv


# 0: name, 1: tettsted nr in muni, 2: tettsted nr
def __get_row_more_than_one(row, name):
    new_row = [name[5:].replace(" i alt", ""), name[:4] + row[1][:4], name[:4]]

    return new_row


def __get_row_one(row):
    new_row = [row[0][5:].replace(" i alt", ""), row[0][:4], row[0][:4]]

    return new_row


# 0: name, 1: tettsted nr, 2: population; 3: area
def __get_normal_row_meta(row):
    new_row = [row[0][5:].replace(" i alt", ""), row[0][:4], row[2].replace(" ", ""), row[4]]

    return new_row


# 0: muni name, 1: muni nr, 2: population; 3: area
def __get_split_row_meta(row):
    new_row = [row[1][5:], row[1][:4], row[3].replace(" ", ""), row[5]]

    return new_row


def print_metadata_tettsted():
    with open('tettsted2022.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if row[0] != "":
                new_row = __get_normal_row_meta(row)

                last_tettsted_nr = new_row[1]

                print("|" + new_row[1] + "=" + new_row[2] + " <!--" + new_row[0] + "-->")

            else:
                new_row = __get_split_row_meta(row)
                print("|" + last_tettsted_nr + new_row[1] + "=" + new_row[2] + " <!--Kommune " + new_row[0] + "-->")

def print_metadata_tettsted_area():
    with open('tettsted2022.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if row[0] != "":
                new_row = __get_normal_row_meta(row)

                last_tettsted_nr = new_row[1]

                print("|" + new_row[1] + "=" + new_row[3].replace(",", ".") + " <!--" + new_row[0] + "-->")

            else:
                new_row = __get_split_row_meta(row)
                print("|" + last_tettsted_nr + new_row[1] + "=" + new_row[3].replace(",", ".") + " <!--Kommune " + new_row[0] + "-->")


def get_tettsted_list_muni(muni_nr):
    list = []

    with open('tettsted2022.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if row[1] == "":  # e.g. "0022 Fredrikstad/Sarpsborg i alt;;"
                tettsted = row[0]
            elif str(muni_nr) in row[1]:
                if row[0] == "":
                    row[0] = tettsted
                    new_row = __get_row_more_than_one(row, tettsted)
                else:
                    new_row = __get_row_one(row)
                list.append(new_row)

    return list


def get_tettsted_by_tettsted_nr(tettsted_nr):
    list = []
    next = False

    with open('tettsted2022.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if next and row[0] == "":
                new_row = ["", "", row[1][:4], row[3].replace(" ", ""), row[5]]

                list.append(new_row)
            else:
                next = False

            if tettsted_nr in row[0]:
                new_row = [row[0][:4], row[0][5:].replace(" i alt", "")]

                if row[1] == "":
                    new_row.append("")  # muni nr
                    next = True
                else:
                    new_row.append(row[1][:4])  # muni nr

                new_row.append(row[2].replace(" ", ""))  # population
                new_row.append(row[4])  # area

                list.append(new_row)

    return list

def write_tettsteder_muni(muni_nr, name):
        list = get_tettsted_list_muni(muni_nr)

        if len(list) == 0:
            return "In der gesamten Gemeinde liegen keine [[Tettsted]]er, also keine Ansiedlungen, die für " \
                   "statistische Zwecke als eine Ortschaft gewertet werden." \
                   "<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

        if len(list) == 1:
            row = list[0]

            text = row[0] + " ist der einzige sogenannte [[Tettsted]], also die einzige Ansiedlung, die für " \
                            "statistische Zwecke als eine Ortschaft gewertet wird."

            if row[1] == row[2]:
                text += " Zum {{EWD|Ort NO|}} lebten dort {{EWZ|Ort NO|" + row[
                    1] + "}} Einwohner.<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"
            else:
                text += " Zum {{EWD|Ort NO|}} lebten in der Kommune " + name + " {{EWZ|Ort NO|" + row[
                    1] + "}} der insgesamt {{EWZ|Ort NO|" + row[
                            2] + "}} Einwohner des Tettsteds.<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

            return text

        if len(list) == 2:
            r1 = list[0]
            r2 = list[1]

            text = "In der Gemeinde liegen zwei sogenannte [[Tettsted]]er, also zwei Ansiedlungen, die für " \
                   "statistische Zwecke als eine Ortschaft gewertet werden. Diese sind "

            if r1[1] == r1[2]:
                text += r1[0] + " mit {{EWZ|Ort NO|" + r1[1] + "}} und "
            else:
                text += r1[0] + " mit {{EWZ|Ort NO|" + r1[1] + "}} der insgesamt {{EWZ|Ort NO|" + r1[
                    2] + "}} Einwohner des Tettsteds und "

            if r2[1] == r2[2]:
                text += r2[0] + " mit {{EWZ|Ort NO|" + r2[1] + "}} Einwohnern"
            else:
                text += r2[0] + " mit {{EWZ|Ort NO|" + r2[1] + "}} der insgesamt {{EWZ|Ort NO|" + r2[
                    2] + "}} Einwohner des Tettsteds"

            return text + " (Stand: {{EWD|Ort NO|}}).<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

        text = "In der Gemeinde liegen mehrere sogenannte [[Tettsted]]er, also mehrere Ansiedlungen, die für" \
               " statistische Zwecke als eine Ortschaft gewertet werden. Diese sind "

        for i in range(len(list)):
            row = list[i]

            if i < len(list) - 1:
                if row[1] == row[2]:
                    text += row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}}, "
                else:
                    text += row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}} der insgesamt {{EWZ|Ort NO|" + row[
                        2] + "}} Einwohner des Tettsteds, "
            else:
                if row[1] == row[2]:
                    text += " und " + row[0] + " mit {{EWZ|Ort NO|" + row[1] +\
                            "}} Einwohnern (Stand: {{EWD|Ort NO|}}).<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}" \
                            "</ref>"
                else:
                    text += " und " + row[0] + " mit {{EWZ|Ort NO|" + row[1] + "}} der insgesamt {{EWZ|Ort NO|" + row[
                        2] + "}} Einwohner des Tettsteds (Stand: {{EWD|Ort NO|}})." \
                             "<ref>{{Metadaten Einwohnerzahl Ort NO||QUELLE}}</ref>"

        return text