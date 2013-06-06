#Renews database with ANEW
import csv
from decimal import Decimal

sr = csv.reader(open("anew.csv", "r"))
data_sr = [(row[0], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in sr]
d = open("testdoc.csv","r")
dr = csv.reader(d)
data_dr = [row[0] for row in dr]
d = open("testdoc.csv","w")
dw = csv.writer(d)

def searchWord(target):
	for x in data_sr:
		if x[0] == target:
			return x
	return None

for word in data_dr:
	f = searchWord(word)
	print f
	if f != None:
		dw.writerow(f)
	else:
		pass

print searchWord('happy')
