#Updates word content in database
import csv

d = open("db.csv","r")
dr = csv.reader(d)
data_dr = [row[0] for row in dr]
d = open("newdb.csv","w")
dw = csv.writer(d, lineterminator = '\n')
words = []

def check(word):
	for r in data_dr:
		if r == word:
			return False
	return True
def byHand ():
	synset = (raw_input("Enter synset name: ")).lower()
	w = (raw_input("Enter word: ")).lower()
	while w != "quit":
		if check(w):
			dw.writerow((w,synset))
			w = (raw_input("Enter word: ")).lower()
		else:
			print "Word already exists."
			w = (raw_input("Enter word: ")).lower()
	if w == "back":
		byHand()
byHand()