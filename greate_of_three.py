def main():
	import sys
	a = sys.stdin.readline()
	b = sys.stdin.readline()
	c = sys.stdin.readline()
	li = []

	li.append(a)
	li.append(b)
	li.append(c)

	sys.stdout.write(max(li))

main()