import csv
from operator import itemgetter
import msvcrt

cr = csv.reader(open("testdoc.csv", "r"))
data = [(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
data.sort(key = itemgetter(0))
#Data is sorted list

allWords = [] #Full list of Synsets and found words (Synset, [words])
val = []
vadsd = []
ar = []
arsd = []


def displayDB():
#Display Words and Information
	for x in data:
		print x[0],':',x[1:]

def addToPile(target):
#Adds word to records
	pass

def searchWord(target):
#Returns tuple with target word and information, None otherwise
	for x in data:
		if x[0] == target:
			# addToPile(target)
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
2. Document Analysis
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
	pass
elif answer == "3":
	displayDB()
