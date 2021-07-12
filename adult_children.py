def adult_child(baccha):
    if baccha<14:
        print("drink toddy")
    elif baccha<18:
        print("they drink coke")
    elif baccha<21:
        print("they drink beer")
    else:
        print("they drink wisky")
adult_child(int(input("enter the age=")))