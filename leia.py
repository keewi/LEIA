import csv
from operator import itemgetter
import math

cr = csv.reader(open("db.csv", "r"))
data = [(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in cr]
data.sort(key = itemgetter(0))
#Data is sorted list of database

keys = []
pile = {} #{Synset : [[Vals], [Ars], [Words], freq]}
aP = {} #{Synset : [Val, Ar, [Words], freq]}
total = []
neg = False

def reset():
	del keys[0:len(keys)]
	pile.clear()
	aP.clear()
	del total[0:len(total)]
	neg = False

def displayDB():
#Display Words and Information
	for x in data:
		print x[0],':',x[1:]

def totalVA():
	t0 = []
	t1 = []
	for k in keys:
		for num in pile[k][0]: 
			t0.append(num)
		for num in pile[k][1]: 
			t1.append(num)
	total.append(avg(t0))
	total.append(avg(t1))

def addToPile((word,synset,val,valsd,ar,arsd)):
#Adds word to records. NEED TO DO: ADD IN SD's!
	global neg
	if neg:
		neg = False
		val = 10-val #SUPER IMPORTANT!! How big is the scale? (Here, it is assumed that it is 1-10)
		ar = 10-ar
		word = "not "+word
	if synset in keys:
		(pile[synset][0]).append(val)
		(pile[synset][1]).append(ar)
		if word not in pile[synset][2]:
			(pile[synset][2]).append(word)
		(pile[synset][3]) += 1
	else:
		keys.append(synset)
		pile[synset] = [[val], [ar], [word], 1]

def unpunctuate(word):
#recurse to find and keep characters, recycle rest (out of ascii range)
	if len(word) > 0:
		c = word[0]
		ascii = ord(c)
		if (ascii>64 and ascii<91) or (ascii>96 and ascii<123):
			return c + unpunctuate(word[1:])
		return unpunctuate(word[1:])
	#should some punctuation be defined as modifiers? (ex. ! vs .)
	return ""

def negFound(word):
#Stores negation found!
	if word == "not":
		global neg 
		neg = True

def searchWord(target):
#Returns tuple with target word and information, None otherwise
	target = unpunctuate(target)
	negFound(target)
	for x in data:	
		if x[0] == target:
			addToPile(x)
			return x
	return None

def avg(list):
#Returns average of a list of numbers
	if len(list)>0:
		avg = (sum(list)/len(list))
		return math.ceil(avg*100)/100
	return 0

def analyzePile():
#Analyzes pile, saves as aP
	for synset in keys:
		aP[synset] = [avg(pile[synset][0]), avg(pile[synset][1]), pile[synset][2], pile[synset][3]]

def displayAnalyzed():
#Prints results
	print "\nRESULTS: "
	print "Synset\tFreq.\tAvg.Valence\tAvg.Arousal\tWords"
	for s in keys: #need to do: make this a nicer-looking table
		print s, "\t", aP[s][3],"\t",aP[s][0],"\t\t",aP[s][1],"\t\t",aP[s][2]

def dataAnalysis():
	doc = raw_input("Document name (must be .csv): ")
	try:
		with open(doc, 'r') as f:
			reader = csv.reader(f)
			d = open("results.csv","w")
			dw = csv.writer(d, lineterminator = '\n')
			# nw = csv.writer(open("newWordsFound.csv","w"), lineterminator = '\n')
			dw.writerow(['Input', 'Analysis', 'Overall Valence', 'Overall Arousal'])
			
			for row in reader:
				for x in row:
					reset()
					text = x.lower()
					words = text.split()
					for s in words:
						searchWord(s)
					analyzePile()
					totalVA()
					dw.writerow([x, aP, total[0], total[1]])
					#THIS IS FOR ADDING NEW WORDS!!(below) - also, the nw line above
					# if len(keys) == 0:
					# 	print x
					# 	newWords = ((raw_input("\nInput new emotion words: ")).lower()).split()
					# 	for w in newWords:
					# 		nw.writerow([w])

			print "\nDone! Results have been saved as results.csv"
	
	except IOError:
		print "Could not read file: ", doc


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
	text = (raw_input("Enter passage: ")).lower()
	for s in words:
		searchWord(s)
	analyzePile()
	displayAnalyzed()

elif answer == "3":
#Searches for words in passages in a csv file
	dataAnalysis()

elif answer == "4":
	displayDB()

# input("Press Enter when done...")#Enable when directly running