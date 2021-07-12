def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    c=a/b 
    return c
def main():
    if sym=="+":
        print(add(a,b))
    elif sym=="-":
        print(sub(a,b))
    elif sym=="*":
        print(multiply(a,b))
    else:
        print(divide(a,b))
a=int(input("enter the num="))
b=int(input("enter the num="))
sym=input("enter the sym=")
main()

