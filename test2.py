""" def staircase(n):
	i = 0
    while i < n:
        print(' ' * (n-i-1) + '#' * (i+1))
        i += 1
staircase(6)b """

def miniMaxSum(arr):
    i = minisum = maxsum = sumtotal = 0
    sumarray = []
    for j in range(len(arr)):
       sumarray.append(0)
    while i < len(arr):
        sumtotal += arr[i]
        i +=1
    for k in range (0,len(arr)):
        sumarray[k] = sumtotal - arr[k]
        k += 1
    maxsum = max(sumarray)
    minisum = min(sumarray)
    print(minisum, maxsum)

a =[1,3,2,6,4]
miniMaxSum(a)