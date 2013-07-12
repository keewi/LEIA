#Renews database with ANEW
import csv
import wx
from decimal import Decimal
from operator import itemgetter



def order():
	data_dr.sort(key = itemgetter(2))

def searchWord(target):
	for x in data_sr:
		if x[0] == target:
			return x
	return None
def run():
	d = open("db.csv","r")
	dr = csv.reader(d)
	data_dr = [(row[0],row[1],row[2],row[3],row[4],row[5]) for row in dr]

	d = open("db.csv","w")#call it newdb.csv to make a new one if revising code
	dw = csv.writer(d, lineterminator = '\n')order()
	try:
		with open('anew.csv', 'r') as f:
			sr = csv.reader(f)
			data_sr = [(row[0], float(row[2]), float(row[3]), float(row[4]), float(row[5])) for row in sr]

		for word in data_dr:
			f = searchWord(word[0])
			if f != None:
				a = list(f)
				a.insert(1, word[1])
				dw.writerow(a)
			else:
				a = list(word)
				dw.writerow(word)
		msg = wx.MessageDialog(None, "Database sync complete.","Completed",wx.OK)
		msg.ShowModal()
		msg.Destroy()
	except IOError:
		msg = wx.MessageDialog(None, "Unknown error: Unable to sync database.","ERROR",wx.OK|wx.ICON_ERROR)
		msg.ShowModal()
		msg.Destroy()