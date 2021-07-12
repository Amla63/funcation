def prime(num):
    i=1
    count=0
    while i<=num:
        if num%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("it is prime num")
    else:
        print("it is not a prime num")
num=int(input("enter the num"))
prime(num)

