import csv
from operator import itemgetter
import bisect

cr = csv.reader(open("testdoc.csv", "r"))
data = [(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
data.sort(key = itemgetter(0))
data2 = {}
for row in data:
	data2[row[0]] = row[1:]
#Data is sorted list
#Data2 is dictionary of words : info

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

def fast_searchWord(target):
#Returns tuple with target word's information, None otherwise
	if target in data2:
		return data2[target]
	return None

def sortWords():
#Returns sorted array (words first)
	data = [(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
	data.sort(key = itemgetter(0))

def sortSynsets():
#Returns sorted array (synsets first)
	data = [(row[1], row[0], int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in cr]
	data.sort(key = itemgetter(0))

print fast_searchWord('happy')

