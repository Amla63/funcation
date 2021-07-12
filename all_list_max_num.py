# ist=[[3,5,65,7],[7,9,12,15,28][6,78,90,98][9,78,67,56,65],[78,56,45,34,100,200]]
# op/[65,28,98,78,200] mins in all list i want max namber
def max(num):
    i=0
    a=[]
    while i<len(num):
        j=0
        max=0
        while j<len(num[i]):
            if num[i][j]>max:
                max=num[i][j]
            j=j+1
        a.append(max)
        i=i+1
    print(a)
max(num=[[3,5,65,7],[7,9,12,15,28],[6,78,90,98],[9,78,67,56,65],[78,56,45,34,100,200]])