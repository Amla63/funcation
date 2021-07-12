def numbers(num):
    i=1
    while i<=num:
        if i%3==0 and i%5==0:
            print(i,"fizzbuzz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"buzz")
        else:
            print(i)
        i=i+1
numbers(int(input("enter the num")))
