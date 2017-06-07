def duplicate_count(text):
	text1 = text.lower()
	fin = set()

	for i in text1:
		num = text1.count(i)
		if num > 1:
			fin.update(i)
	return len(fin)

duplicate_count("mandelan")