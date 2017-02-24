name = {'sea':'water','sun':'Hot'}
while True:
	word = raw_input("Enter word to check its meaning: ")
	
	if word == "":
		break
	elif word not in name:
		print "Word not found, please add its meaning"
		nw = raw_input(": ")
		name[word] = nw
	else:
		print name[word]
