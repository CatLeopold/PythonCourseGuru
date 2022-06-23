list=["a","b","c","d","e"]
i=0
while i<len(list):
    print(""+str(i)+"-"+list[i])
    i+=1
print(len(list))
while True:
    a=int(input("Введите индекс того элемента, значение которого вы хотите посмотреть"))
    if a>len(list)-1:
        print("Элемента с таким индексом не существует")
    else:
        print("Значение элемента с индексом",a,"=", list[a])

