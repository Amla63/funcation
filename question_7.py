def function_name(name1,name2):
    a=len(name1)
    b=len(name2)
    if a==b:
        print(name1)
        print(name2)
    elif a>b:
        print(name1)
    else:
        print(name2)
function_name(name1=input("enter the name="),name2=input("enter the name="))



