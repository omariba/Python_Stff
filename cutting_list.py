##v = input("::")
##
##first = range(1,v+1)
##first.reverse()
##
##stop = ""
##
##while stop != "s":
##    try:
##        print first
##
##        me = first[3]
##        us = first[0]
##        you = us - me
##
##        first = range(1,you+1)
##        first.reverse()
##        print you
##    except:
##        stop = "s"

##def answer(area):
##    import math
##    the_number= 0
##    squares = []
##    for number in range(area-1, 0, -1):
##        root = math.sqrt(number)
##        if root.is_integer():
##            # print the_number
##            squares.append(number)
##    number = area - number
##        # elif sum(squares) == area:
##
##    return squares
##print answer(12)

##area = input()
##def answer(area):
##    val = []
##    import math
##    test = range(area)
##    test.reverse()
##    for n in test:
##        if math.sqrt(n).is_integer():
##            new_m = n
##            val.append(n)
##            break
##        area = test[0] - new_m
##    print val


num = input("::")
us = range(1,num+1)

tot = 0

for i in us:
   tot += i

print tot

