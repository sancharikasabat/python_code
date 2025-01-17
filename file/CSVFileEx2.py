import csv
with open("C:\\Users\\sanch\\csv\\student.csv") as fp:
    csvr=csv.reader(fp) #csvr is object class of csv.reader
    for rec in csvr :
        for val in rec:

            print("{}".format(val),end="\t")
        print()   
