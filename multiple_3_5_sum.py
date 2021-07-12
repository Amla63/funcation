def sum(limit):
    i=0
    sum=0
    while i<limit:
        if i%3==0 or i%5==0:
            print(i)
            sum=sum+i
        i=i+1
    print(sum,"total sum")
sum(int(input("enter the num")))

# list=[[1,2,3],[4,5,6]]
# i=0
# while i<=len(list):
#     j=0
#     s=1
#     while j<len(list):
#         s=list[j][i]*s
#         j=j+1
#     i=i+1
#     print(s)