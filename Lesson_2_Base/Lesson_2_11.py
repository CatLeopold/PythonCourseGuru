import random
siselist=int(input("Введите размер списка:"))
arr=[int(random.random()*100) for i in range(0,siselist)]
print(arr)
i=0
while i<len(arr):
    print(arr[i])
    i+=1
arr=list(set(arr))
print(arr)
lenarr=len(arr)
print("длина массива после очистки=",lenarr)
for q in arr:
    print(q)
