def group_check(s):
    bracks = ['(',')','[',']','{','}']
    if len(s)%2 !=0:
        print "Done incorrectly"
    else:
    	for t in s:
    		if t in bracks:
    			if t == '}':
    				pass
    			elif bracks[bracks.index(t)+1] in s[s.index(t)+1:]:
    				pos = s.index(bracks[bracks.index(t)])
    				pos1 = s.index(bracks[bracks.index(t)+1])
    				
    				if len(s[pos:pos1+1])%2 != 0:
    					print "Done incorrectly"
    				else:
    					print "Done correctly"
    				
##    				print s.index(bracks[bracks.index(t)+1]) - s.index(bracks[bracks.index(t)])   
 				  
##        for n,b in enumerate(s):
##          for i in bracks:
##              if i == s and bracks[bracks.index(i)+1] in s[n+1:]:
##                  print "yeahh.. True!"
##        if bracks[0] in s and bracks[1] in s[s.index(bracks[0])+1:]:
##            print bracks[0],bracks[1]
##        elif bracks[2] in s and bracks[3] in s[s.index(bracks[2])+4:]:
##            print bracks[2],bracks[3]
##        for b,c in zip(s,bracks):
##            if b == c and s.index(b)+1 == bracks.index(c)+1
##        i = 0
##        while i < len(s)-1:
##            if s[i] == a and s[i+1] == a1:
##                print s[i],s[i+1]
##            i+=1
##        for i in range(len(s)-1):
##            if s[i] == s[i+1]:
##                print s[i],s[i+1]

group_check("({[]}]")
