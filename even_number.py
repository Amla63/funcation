def show_number(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
show_number(int(input("enter the num")))