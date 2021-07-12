def even(num):
    i=0
    b=[]
    while i<len(num):
        if num[i]%2==0:
            b.append(num[i])
        i=i+1
    print(b)
num=[1,2,3,4,5,6,7,8,9]
even(num)