import csv

d = csv.reader(open('db.csv','r'))
data = [(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in d]
keys = []
synsets = {}

def synAvg():
	c = ""
	for word in data:
		if (c != "") and (word[1] != c):
			pass
		else:
			pass