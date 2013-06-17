#Renews database with ANEW
import csv
from decimal import Decimal

sr = csv.reader(open("anew.csv", "r"))
data_sr = [(row[0], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in sr]

d = open("db.csv","r")
dr = csv.reader(d)
data_dr = [(row[0],row[1],row[2],row[3],row[4],row[5]) for row in dr]

d = open("db.csv","w")#call it newdb.csv to make a new one if revising code
dw = csv.writer(d, lineterminator = '\n')

def searchWord(target):
	for x in data_sr:
		if x[0] == target:
			return x
	return None

for word in data_dr:
	f = searchWord(word[0])
	if f != None:
		a = list(f)
		a.insert(1, word[1])
		dw.writerow(a)
	else:
		a = list(word)
		dw.writerow(word)

print "Done!"