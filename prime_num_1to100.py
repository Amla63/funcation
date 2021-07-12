def prime(num):
    i=1
    while i<=100:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c+=1
            j=j+1
        if c==2:
            print(i)
        i=i+1
prime(100)