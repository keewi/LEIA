import csv
from operator import itemgetter
import math

#IMPORT DATABASE
cr = csv.reader(open("db.csv", "r"))
data = [(row[0], row[1], row[2],row[3],row[4],row[5]) for row in cr]
data.sort(key = itemgetter(2))
blankdata = []
for row in data: #takes out all blanks and puts into blankdata, for future use
	if row[2]=='':
		blankdata.append(row)
		data = data[1:]
	else:
		break
data = [(row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for (row) in data]
data.sort(key = itemgetter(0))
#Data is sorted list of database

#GLOBAL VARIABLES
keys = [] #Found synsets
pile = {} #Found words and synsets. Format: {Synset : [[Vals], [Ars], [Words], freq]}
aP = {} #Aggregate pile. Format: {Synset : [Calculated Val, Calculated Ar, [Words], freq]}
total = [] #Total V/A per full text
neg = False #Negation found = FALSE
punc = ["?",".", ",",":",";","!"] #Recognized as punctuation characters
p = False #Punctuation found = FALSE
very = False #Intensifier found = FALSE
vList = ["very","extremely", "really","max","too"] #Recognized intensifiers
alittle = False #Unintensifier found = FALSE
aList = ["little","kind","sort","pretty","somewhat","slightly","rather","mildly"] #Recognized unintensifiers
conj = ["but","and","or","yet","nor","for","also","so","any"] #Recognized conjunctions
#NOTE: When adding new types of modifiers, add to 7 places. This is the first place. Mod(1/7)
#FUTURE CHANGES: add queue to make it so the order modifiers are found can be preserved and used

def reset():
#Resets variables. Used after every full text analysis
	del keys[0:len(keys)]
	pile.clear()
	aP.clear()
	del total[0:len(total)]
	global neg, p, very, alittle
	p, neg, very, alittle = (False,)*4 #Mod(2/7)

def getSize():
	return len(data)

def displayDB():
#Prints Words and Information
	print "\nFORMAT: \nword : ('synset', valence, val sd, arousal, ar sd)\n"
	for x in data:
		print x[0],':',x[1:]

def totalVA():
#Analyzes and records total entry valence and arousal
	t0, t1 = [], []
	for k in keys:
		t0.extend(pile[k][0])
		t1.extend(pile[k][1])
	total.append(calc(t0)) #Uses current calc function for Overall Valence
	total.append(max(t1)) #Uses maximum function for Overall Arousal

def addToPile((word,synset,val,valsd,ar,arsd)):
#Adds word to records.
	#Apply mofidiers
	global neg, very, alittle #Mod(3/7)
	delta = 0
	if very: #if intensifier found = TRUE, emphasizes by 1
		very = False
		if val > 5: delta += 1
		else: delta -= 1
		word = "very "+word	
	if alittle: #if unintensifier found = TRUE, de-emphasizes by 1
		alittle = False
		if val > 5: delta -= 1
		else: delta += 1
		word = "a little "+word
	if neg: 
		neg = False
		if val > 5: delta -= (val-4.5)*1.3
		else: delta += (4.5-val)*1.3 #Not very sad, not very surprised
		# val = 9-val #Sets so that negations flips val/ar
		# ar = 9-ar
		word = "not "+word

	val = val + delta #Note: modifications are based off ORIGINAL valences, before negations
	ar = ar + delta
	#Mod(4/7): add changes to val/ar/word
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
	global p
	if len(word) > 0:
		c = word[0]
		ascii = ord(c)
		if (ascii>64 and ascii<91) or (ascii>96 and ascii<123):
			return c + unpunctuate(word[1:])
		if (c in punc):
			p = True #Removes overflow for negations into following sentences
		return unpunctuate(word[1:])
	#should some punctuation be defined as modifiers? (ex. ! vs .)
	return ""
	
def searchWord(target):
#Returns tuple with target word and information, None otherwise
	global neg, very, p, alittle #Mod(5/7)

	target = unpunctuate(target)
	if (target == "not") or (target[-3:] == "dnt" or target[-3:] == "snt"): #Ref: 51, 285
		neg = True
	elif (target in vList): #Is it an intensifier?
		very = True
	elif (target in aList): #Is it an unintensifier?
		alittle = True
	#Mod(6/7)
	elif (target in conj): #Resets after a "but" (ex. didn't win, but is happy)
		very, neg, alittle = (False,)*3
	found = None
	for x in data:
		#Looks for word in database
		if x[0] == target:
			addToPile(x)
			found = x
	if p:
		p, neg, very, alittle = (False,)*4 #Mod(7/7)
	return found

def calc(list):
#Returns calculation: average
	if len(list)>0:
		avg = (sum(list)/len(list))
		return math.ceil(avg*100)/100
	return 0

def max(list):
	max = 0
	if len(list)>0:
		for elem in list:
			if elem > max: max = elem
	return max

def textAnalysis(text):
#Analyzes a single passage
	reset()
	text = text.lower()
	words = text.split()
	for s in words:
		searchWord(s)
	#Analyzes pile, saves as aP
	for synset in keys:
		aP[synset] = [calc(pile[synset][0]), calc(pile[synset][1]), pile[synset][2], pile[synset][3]]
	totalVA()

def dataAnalysis(results):
#Analyzes each and every entry in a document separately
	doc = raw_input("Document name (must be .csv): ")
	try:
		with open(doc, 'r') as f:
			reader = csv.reader(f)
			d = open(results,"w")
			dw = csv.writer(d, lineterminator = '\n')
			dw.writerow(['Input', 'Analysis', 'Overall Valence', 'Overall Arousal'])
			for row in reader:
				for x in row:
					textAnalysis(x)
					dw.writerow([x, aP, total[0], total[1]])
			print "\nDone! Results have been saved as results.csv"
	except IOError:
		print "Could not read file: ", doc
def opt1(word):
	target = word.lower()
	find = searchWord(target)
	if find == None:
		print "Not found.\n"
	else:
		print "Synset:          ", find[1]
		print "Valence:        ", find[2]
		print "Valence(sd):  ", find[3]
		print "Arousal:         ", find[4]
		print "Arousal(sd):  ", find[5]
		print ""

def opt2(text):
	textAnalysis(text)
	print "OVERALL VALENCE: ",total[0]
	print "OVERALL AROUSAL: ",total[1]
	print "DETAILED RESULTS:"
	print "Synset\t\tFreq.\tAvg.Valence\tAvg.Arousal\tWords"
	for s in keys: #NEED TO DO: make the spacing work
		print s, "\t\t", aP[s][3],"\t",aP[s][0],"\t\t",aP[s][1],"\t\t",aP[s][2]
	print ""

def opt3(docname, results):
	try:
		with open(docname, 'r') as f:
			reader = csv.reader(f)
			d = open(results,"w")
			dw = csv.writer(d, lineterminator = '\n')
			dw.writerow(['Input', 'Analysis', 'Overall Valence', 'Overall Arousal'])
			for row in reader:
				for x in row:
					textAnalysis(x)
					dw.writerow([x, aP, total[0], total[1]])
			return True
			print "Done! Results have been saved as results.csv"
	except IOError:
		return False
		# print "Could not read file: ", docname