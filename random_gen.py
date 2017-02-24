import random
import os
import time

#generate once

#name = ""
#li = []
#while name != "00":
#	name = raw_input("Items: ")
#	if name == "00":
#		pass
#	else:
#		li.append(name)

#li = ['Gitonga','Mandela','Kevin','Kimani','Cetric','Robert']
#def gen():
#	random.shuffle(li)
#	for i in li:
#		print i
#gen()

#randomise from a file

def gen():
	try:
		import docx
	except:
		print "Please type the command 'pip install docx' to continue"
	file_name = raw_input("Enter the file name to randomise words from: ")

	if file_name.endswith("docx"):
		acc = open(file_name,"r")
		file_obj = acc.xreadlines()
		open_docx = docx.opendocx(file_obj)
		data = docx.getdocumenttext(open_docx)
		random.shuffle(data)
		for i in data:
			if i == "\n":
				pass
			else:
				print i
				time.sleep(0.5)

	else:
		acc = open(file_name,"r")
		li = acc.readlines()
		acc.close()
	
		random.shuffle(li)
		for i in li:
			if i == "\n":
				pass
			else:
				print i
				time.sleep(0.5)
		
gen()

#path = os.getcwd()
#file_in = path + file_name
