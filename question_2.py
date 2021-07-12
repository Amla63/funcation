def perfect(a):
    i=1
    s=0
    while i<a:
        if a%i==0:
            s=s+i
        i=i+1
    if s==a:
        print(a,"is perfect num")
for i in range(1,1000):
    perfect(i)
