def poss(word):
	vowel = ['A','E','I','O','U','Y','a','e','i','o','u','y']
	for i in word:
		if i in vowel:
			if i == "Y" or i == "y":
				if word.index(i) == 0:
					continue
			else:
				return word.index(i)
					#return word.index(i)
					#break
			#else:
			#	print word.index(i)
				#return word.index(i)
			#	break
#		else:
#			pass
			#return -1
			
print poss('yesterday')
