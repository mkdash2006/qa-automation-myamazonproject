import csv

def csvhandling(filepath):
    with open(filepath) as data:
        formttedcsvdata = csv.DictReader(data)
        values= []
        for i in formttedcsvdata:
            values.append(i)
        return values