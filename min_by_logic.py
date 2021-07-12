def min(numbers):
    i=0
    min=numbers[0]
    while i<len(numbers):
        if numbers[i]<min:
            min=numbers[i] 
        i=i+i
    print(min)
numbers=[3,6,8,5,4,3,2,1]
min(numbers)