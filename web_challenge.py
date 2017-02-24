for i,j in enumerate(sml):
	if j in string.uppercase:
		if j == sml[i+1] and j == sml[i+2]:
			if sml[i+3] in string.lowercase:
				if j == sml[i+4] and j == sml[i+5]:
					if j == sml[i+6]:
						word.append(j)
						print word

