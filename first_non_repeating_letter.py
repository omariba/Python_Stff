def first_non_repeating_letter(string):
	string1 = string.lower()
	s = []
	c = []
	if len(string1) !=0:
		for i in string1:
			c.append(string1.count(i))
			if string1.count(i) == 1:
				l = string1.index(i)
				s.append(string[l])
				return s[0]
		if all( f > 1 for f in c):
			return ""

	else:
		return ""


first_non_repeating_letter(string)