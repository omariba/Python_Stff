import math

def average_string(s):
	ref = {"zero":0,"one":1,
		"two":2,"three":3,
		"four":4,"five":5,
		"six":6,"seven":7,
		"eight":8,"nine":9
		}
	num = []
	if len(s) == 0:
		return 'n/a'
	else:
		temp = s.split(' ')
		for w in temp:
			if w in ref.iterkeys():
				num.append(ref[w])
			else:
				return 'n/a'
		ans = math.trunc(sum(num)/len(num))
		for key, value in ref.iteritems():
			if value == ans:
				return key

average_string('two eight nine')
