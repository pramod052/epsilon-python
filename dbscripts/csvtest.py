import csv

myreader = csv.reader(open("studentrecord.txt","r"))

for row in myreader:
	print(row[1])
