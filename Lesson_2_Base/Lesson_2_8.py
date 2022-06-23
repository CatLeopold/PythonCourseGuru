s = 0
while True:
    a = input('Введите число\nили слово "sum" для суммирования чисел\nили слова "exit" или "quit" для завершения: ')
    if a == "exit" or a == "quit":
        print()
        break
    if a == "sum":
        print("Сумма введенных чисел=", s)
        print('_________________')
        s = 0
    else:
        s += int(a)
