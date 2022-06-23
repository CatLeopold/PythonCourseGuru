def ismax(arr):
    max=arr[0]
    for n in arr:
        if n>max:
            max=n
    return max

def ismin(arr):
    min=arr[0]
    for n in arr:
        if n<min:
            min = n
    return min

def summa(arr):
    sum=0
    for n in arr:
        sum+=n
    return sum

# для проверки
#print(ismax([10,1,20,4]))
#print(ismin([10,1,20,4]))
#print(summa([10,1,20,4]))