import csv
f= open("Book3.csv")

csv_f=csv.reader(f);
for row in csv_f:
    print (row)
f.close()
