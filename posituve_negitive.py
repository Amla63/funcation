def positive_negitive(num):
    i=0
    c_positive=0
    c_negitive=0
    while i<len(num):
        if num[i]>0:
            c_positive+=1
        elif num[i]<0:
            c_negitive+=1
        i=i+1
    print(c_positive)
    print(c_negitive)
positive_negitive([2,-7,5,-64,-14])
