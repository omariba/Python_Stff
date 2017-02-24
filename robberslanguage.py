word = raw_input('enter any sentence: ')
def translate(word):
	li = ['a','e','i','o','u']
	con = 'o'
	
	new_set = []

	for n in word:
		if n not in li and  n != " ":			
				dou = n+con+n
				new_set.append(dou)
		else:
			new_set.append(n)
	print ''.join(new_set)
translate(word)
