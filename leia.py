import csv
from operator import itemgetter

cr = csv.reader(open("db.csv", "r"))
data = [(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in cr]
data.sort(key = itemgetter(0))
#Data is sorted list

keys = []
pile = {}

def displayDB():
#Display Words and Information
	for x in data:
		print x[0],':',x[1:]

def addToPile((word,synset,val,valsd,ar,arsd)):
#Adds word to records
	if synset in keys:
		(pile[synset][0]).append(val)
		(pile[synset][1]).append(ar)
		if word not in pile[synset][2]:
			(pile[synset][2]).append(word)
		# print pile[synset]
		# print "New word added!"
	else:
		keys.append(synset)
		pile[synset] = ([val], [ar], [word])
		# print "New synset added!"

def searchWord(target):
#Returns tuple with target word and information, None otherwise
	for x in data:
		if x[0] == target:
			addToPile(x)
			# print x
			return x
	return None

def sortWords():
#Returns sorted array (words first)
	data = [(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
	data.sort(key = itemgetter(0))

def sortSynsets():
#Returns sorted array (synsets first)
	data = [(row[1], row[0], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
	data.sort(key = itemgetter(0))

print """MENU:
1. Single Word Analysis
2. Text Analysis
3. Display Database
4. Quit\n"""
answer = raw_input("Please choose an option: ") 
#Set as an option if you are only using one

if answer == "1":
	target = (raw_input("Enter word: ")).lower()
	find = searchWord(target)
	if find == None:
		print "Not found."
	else:
		print "\nRESULTS: "
		print "Synset:      ", find[1]
		print "Valence:     ", find[2]
		print "Valence(sd): ", find[3]
		print "Arousal:     ", find[4]
		print "Arousal(sd): ", find[5]

elif answer == "2":
	text = (raw_input("Enter passage: ")).lower() #input text. do/write txt/csv?
	words = text.split()
	# print words
	for s in words:
		searchWord(s)
	print pile

elif answer == "3":
	displayDB()

# input("Press Enter when done...")#Enable when directly running