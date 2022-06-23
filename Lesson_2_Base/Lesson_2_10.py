array=[i+1 for i in range(1,5)]
print(array)
summ=0
x=0
average=0
for q in array:
    print(q)
    summ=summ+q
    x+=1
average=summ/x
print("Сумма чисел массива =",summ)
print("количество значений массива =",x)
print("Средне арифметическое чисел массива =",average)