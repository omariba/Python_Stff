def race(v1, v2, g):
	v3 = v2-v1
	t = float(g)/float(v3)
	h,m,s = 0,0,0
	if t < 1:
		h = 0
		t *= 60
		if t < 1:
			m=0
		elif t >= 1:
			m = int(t)
			t -= m
			t *= 60
			if t < 1:
				s=0
			elif t >= 1:
				s = int(t)
	elif t >= 1:
		h = int(t)
		t -= h
		t *= 60
		if t < 1:
			m=0
		elif t >= 1:
			m = int(t)
			t -= m
			t *= 60
			if t < 1:
				s=0
			elif t >= 1:
				s = int(t)
	a_t = [h,m,s]
	print a_t
race(18, 20, 0.05)