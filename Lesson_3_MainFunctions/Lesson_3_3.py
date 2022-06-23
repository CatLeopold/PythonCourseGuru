list = []
print(list)
try:
    n = int(input("Какое количество элементов надо создать в списке?"))
    x = 0
    while x < n:
        x += 1
        el = int(input("Введите число N:», где N – текущий номер числа."))
        list.append(el)
    print(list)

except ValueError:
    print("Некорректный ввод!")
