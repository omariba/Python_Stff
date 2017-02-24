for num in range(1,20):
    if num == 1:
        print "%s is Not PrimeNumber" %num
    elif num%2 == 0:
        if num ==2:
            print "%s is A PrimeNumber" %num
        else:
            print "%s is Not A PrimeNumber" %num
    elif num%1 == 0 and num%num == 0:
        print "%s Prime" %num

        
