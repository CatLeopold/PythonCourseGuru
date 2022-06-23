a=float(input('Введите первое число:'))
b=float(input('Введите второе число:'))
try:
    x=a/b
except ZeroDivisionError:
    print('бесконечность')
else:
    print(x)

