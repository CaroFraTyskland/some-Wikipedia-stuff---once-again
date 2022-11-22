import csv

#0: name, 1: tettsted nr in muni, 2: tettsted nr
def __get_row_more_than_one(row, name):
    new_row = []
    
    new_row.append(name[5:].replace(" i alt", "")) #tettsted name
    new_row.append(name[:4] + row[1][:4]) #tettsted nr muni
    new_row.append(name[:4]) #tettsted nr
    
    return new_row
    
def __get_row_one(row):
    new_row = []
    
    new_row.append(row[0][5:].replace(" i alt", "")) #tettsted name
    new_row.append(row[0][:4]) #tettsted nr muni
    new_row.append(row[0][:4]) #tettsted nr complete
    
    return new_row

#0: name, 1: tettsted nr, 2: population; 3: area
def __get_normal_row_meta(row):
    new_row = []
    
    new_row.append(row[0][5:].replace(" i alt", "")) #tettsted name
    new_row.append(row[0][:4]) #tettsted nr
    new_row.append(row[2].replace(" ", "")) #population
    new_row.append(row[4]) #area
    
    return new_row

#0: muni name, 1: muni nr, 2: population; 3: area
def __get_split_row_meta(row):
    new_row = []
    
    new_row.append(row[1][5:]) #muni name
    new_row.append(row[1][:4]) #muni nr
    new_row.append(row[3].replace(" ", "")) #population
    new_row.append(row[5]) #area
    
    return new_row


def print_metadata_tettsted():
    with open('tettsted2021.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        last_tetsted_nr = 0
        
        for row in reader:
            if row[0] != "":
                new_row = __get_normal_row_meta(row)

                last_tettsted_nr = new_row[1]

                print ("|" + new_row[1] + "=" + new_row[2] + " <!--"+new_row[0] +"-->")

            else:
                new_row = __get_split_row_meta(row)
                print ("|" + last_tettsted_nr + new_row[1] + "=" + new_row[2] + " <!--Kommune "+new_row[0] +"-->")

def get_tettsted_list_muni(muni_nr):
    list = []

    with open('tettsted2021.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        for row in reader:
            if row[1] == "": #e.g. "0022 Fredrikstad/Sarpsborg i alt;;"
                tettsted = row[0]
            elif str(muni_nr) in row[1]:
                if(row[0] == ""):
                    row[0] = tettsted
                    new_row = __get_row_more_than_one(row, tettsted)
                else:
                    new_row = __get_row_one(row)
                list.append(new_row)            
        
    return list


def get_tettsted_by_tettsted_nr(tettsted_nr):
    list = []
    next = False
    stopAtNextTettsted = False

    with open('tettsted2021.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        for row in reader:
            if next and row[0] == "":
                new_row = []
                new_row.append("") #tettsted nr
                new_row.append("") #tettsted name
                new_row.append(row[1][:4]) #muni nr
                new_row.append(row[3].replace(" ", "")) #population
                new_row.append(row[5]) #area

                list.append(new_row)
            else:
                next = False

            if tettsted_nr in row[0]:
                new_row = []
                new_row.append(row[0][:4]) #tettsted nr
                new_row.append(row[0][5:].replace(" i alt", "")) #tettsted name

                if row[1] == "":
                    new_row.append("") #muni nr
                    next = True
                else:
                    new_row.append(row[1][:4]) #muni nr


                new_row.append(row[2].replace(" ", "")) #population
                new_row.append(row[4]) #area
                    
                list.append(new_row)
        
    return list