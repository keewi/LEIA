import csv
from operator import itemgetter

cr = csv.reader(open("fwDB.csv", "r"))
data = [(row[0], row[1]) for row in cr]
# data.sort(key = itemgetter(0))

dw = csv.writer(open("newfwDB.csv","w"), lineterminator = '\n')

freq = 0
total = 0


def reset():
	freq = 0
	total = 0

def searchWord(target):
	if target in data:
		#store functional word
		freq += 1
	# else:
		#store non-functional word
	total += 1

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

def display():
	print "Articles: ",freq
	print "Total: ",total
def singleSearch():
	text = raw_input("Insert word: ")
	searchWord(text)
	display()

def lower():
	for r in data:
		cat = r[0]
		print cat
		words = []
		for word in r[1]:
			words.append(word.lower())
		dw.writerow([cat, words])

lower()