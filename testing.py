import csv

cr = csv.reader(open("testdoc.csv", "r"))


def displayDB():
#Display Words and Information
	rownum = 1

	for row in cr:
		if (rownum > 1):
			print row[0],":",row
		rownum = rownum+1

def searchWord():
#Search for a single word
	rownum = 1

def sortWords():
#Returns sorted array (words first)
	data = makeData(1)
	return data.sort()

def makeData(code):
	if code = 1:
		#returns words first
		return [(row['word'], row['synset'], int(row['val']), int(row['valsd']), int(row['ar']), int(row['arsd'])) for row in csv.DictReader(cr)]
	else:
		#returns synsets first
		return [(row['synset'], row['word'], int(row['val']), int(row['valsd']), int(row['ar']), int(row['arsd'])) for row in csv.DictReader(cr)]

def sortSynsets():
#Returns sorted array (synsets first)
	data = makeData(2)
	return data.sort()

displayDB()

input("Press Enter to continue...")
