import csv
from operator import itemgetter

cr = csv.reader(open("functionWords.csv", "r"))
data = [row[0] for row in cr]
data.sort(key = itemgetter(0))

def reset():
	pass

def searchWord(target):
	if target in data:
		#store functional word
	else:
		#store non-functional word

def dataAnalysis():
	doc = raw_input("Document name (must be .csv): ")
	try:
		with open(doc, 'r') as f:
			reader = csv.reader(f)
			d = open("results.csv","w")
			dw = csv.writer(d, lineterminator = '\n')

			for row in reader:
				for x in row:
					text = x.lower()
					words = text.split()
					for s in words:
						searchWord(s)
					analyzePile()
					dw.writerow([x, aP])
	
	except IOError:
		print "Could not read file: ", doc

