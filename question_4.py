def show_numbers(limit):
    i=0
    while i<limit:
        if i%2==0:
            print(i,"enen")
        else:
            print(i,"odd")
        i=i+1
limit=int(input("enter the num"))   
show_numbers(limit)