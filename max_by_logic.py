def max(numbers):
    i=0
    max=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    print(max)
numbers=[3,4,6,33,2,7,8,9]
max(numbers)

