# for i in range(20):
# 	if i == 2:
# 		print i
# 	elif i%2 != 0:
		
# for i in range(20,0,-1):
# 	if i%2 == 0:
# 		i/=2

#i = range(10)
#while i >=1:	
#	if i%2 == 0:
#		i+=1
#	else:
#		i/

# li = []
# for m in range(1,21):
# 	for n in range(20,0,-1):
# 		if n*m == 20:
# 			li.append(n)
# 			li.append(m)
# print li


#def primef(n):
#   i = 2
#    while i * i <= n:
#        if n % i:
#            i += 1
#        else:
#            n //= i
#    print n
#primef(30)
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    print n
largest_prime_factor(17)
