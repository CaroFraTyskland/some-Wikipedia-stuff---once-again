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

def get_tettsted_list_muni(muni_nr):
    list = []

    with open('tettsted.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        
        for row in reader:
            if row[1] == "":
                tettsted = row[0]
            elif str(muni_nr) in row[1]:
                if(row[0] == ""):
                    row[0] = tettsted
                    new_row = __get_row_more_than_one(row, tettsted)
                else:
                    new_row = __get_row_one(row)
                list.append(new_row)            
        
    return list