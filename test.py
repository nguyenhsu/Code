def simpleArraySum(ar):
    sum = 0
    i = 0
    while i < len(ar):
        sum += ar[i]
        i += 1
    return sum

b =[1,2,3,4,5,6]
print(simpleArraySum(b))

