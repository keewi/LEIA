import csv
from operator import itemgetter
import math

cr = csv.reader(open("db.csv", "r"))
data = [(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in cr]
data.sort(key = itemgetter(0))
#Data is sorted list

keys = []
pile = {} #{Synset : [[Vals], [Ars], [Words], freq]}
aP = {} #{Synset : [Val, ]}

def reset():
	del keys[0:len(keys)]
	pile.clear()
	aP.clear()

def displayDB():
#Display Words and Information
	for x in data:
		print x[0],':',x[1:]

def addToPile((word,synset,val,valsd,ar,arsd)):
#Adds word to records. NEED TO DO: ADD IN SD's!
	if synset in keys:
		(pile[synset][0]).append(val)
		(pile[synset][1]).append(ar)
		if word not in pile[synset][2]:
			(pile[synset][2]).append(word)
		(pile[synset][3]) += 1
		# print "New word added!"
	else:
		keys.append(synset)
		pile[synset] = [[val], [ar], [word], 1]
		# print pile[synset]
		# print "New synset added!"

def searchWord(target):
#Returns tuple with target word and information, None otherwise
	for x in data:
		if x[0] == target:
			addToPile(x)
			return x
	return None

def analyzePile():
#Analyzes pile, saves as aP
	def avg(list):
		avg = (sum(list)/len(list))
		return math.ceil(avg*100)/100
	for synset in keys:
		aP[synset] = [avg(pile[synset][0]), avg(pile[synset][1]), pile[synset][2], pile[synset][3]]

def displayAnalyzed():
	print "\nRESULTS: "
	print "Synset\tFreq.\tAvg.Valence\tAvg.Arousal\tWords"
	for s in keys: #need to do: make this a nicer-looking table
		print s, "\t", aP[s][3],"\t",aP[s][0],"\t\t",aP[s][1],"\t\t",aP[s][2]


print """MENU:
1. Single Word Analysis
2. I/O Text Analysis
3. Data Analysis
4. Display Database
5. Quit\n"""
answer = raw_input("Please choose an option: ") 
#Set as an option if you are only using one

if answer == "1":
#Searches one word
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
#Searches for words in text input
	text = (raw_input("Enter passage: ")).lower() #input text. do/write txt/csv?
	words = text.split()
	for s in words:
		searchWord(s)
	analyzePile()
	displayAnalyzed()

elif answer == "3":
#Searches for words in passages in a csv file
	doc = raw_input("Document name (must be .csv): ")
	try:
		with open(doc, 'r') as f:
			reader = csv.reader(f)
			d = open("results.csv","w")
			dw = csv.writer(d, lineterminator = '\n')

			for row in reader:
				for x in row:
					reset()
					print "Reset!"
					text = x.lower()
					words = text.split()
					for s in words:
						searchWord(s)
					analyzePile()
					dw.writerow([x, aP])
	
	except IOError:
		print "Could not read file: ", doc

elif answer == "4":
	displayDB()

# input("Press Enter when done...")#Enable when directly running